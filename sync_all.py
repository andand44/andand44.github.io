import os
import json
import re
import time
import requests
from openai import OpenAI
from dotenv import load_dotenv
from slugify import slugify

load_dotenv()

GITHUB_USER = "andand44"
CACHE_FILE = "repo_cache.json"

# Инициализируем клиента OrcaRouter
client = OpenAI(base_url="https://api.orcarouter.ai/v1", api_key=os.getenv("LLM_API_KEY"))
MODEL_NAME = "deepseek/deepseek-v4-flash-free"
USE_LOCAL = False

def get_free_models():
    """Запрашивает у OrcaRouter список доступных бесплатных моделей."""
    print("Ищем доступные бесплатные модели в OrcaRouter...")
    try:
        # Запрашиваем список моделей
        response = requests.get(
            "https://api.orcarouter.ai/v1/models", 
            headers={"Authorization": f"Bearer {os.getenv('LLM_API_KEY')}"}
        )
        if response.status_code == 200:
            models = response.json().get("data", [])
            # Фильтруем только бесплатные (обычно содержат 'free' в названии)
            free_models = [m["id"] for m in models if "free" in m["id"].lower()]
            if free_models:
                print(f"Доступные бесплатные модели: {free_models}")
                return free_models
    except Exception as e:
        print(f"Не удалось получить список моделей: {e}")
    
    # Если не удалось получить список, используем дефолтный список
    print("Используем стандартный список моделей.")
    return ["deepseek/deepseek-v4-flash-free", "orcarouter/free"]

available_models = get_free_models()
current_model_idx = 0

def safe_llm_call(prompt):
    global current_model_idx, USE_LOCAL, client, MODEL_NAME
    
    while True:
        if USE_LOCAL:
            current_model = "qwen3.5:2b" # Локальная модель
        else:
            current_model = available_models[current_model_idx]
        
        try:
            response = client.chat.completions.create(
                model=current_model,
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                temperature=0.2
            )
            return response.choices[0].message.content
            
        except Exception as e:
            err_str = str(e)
            
            # Если это ошибка лимита или недоступности модели
            if "429" in err_str or "404" in err_str or "503" in err_str:
                print(f"  [!] Модель {current_model} недоступна. Ошибка: {err_str[:50]}...")
                
                if not USE_LOCAL:
                    current_model_idx += 1
                    if current_model_idx >= len(available_models):
                        print("\n[!] Все облачные модели перегружены или закончились.")
                        choice = input("Переключиться на локальную Ollama (qwen3.5:2b)? (y/n): ")
                        if choice.lower() == 'y':
                            print("🚀 Переключено на ЛОКАЛЬНУЮ Ollama (может быть медленно).")
                            client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
                            USE_LOCAL = True
                            continue # Продолжаем цикл с локальной моделью
                        else:
                            print("Ожидание 30 секунд перед новой попыткой...")
                            time.sleep(30)
                            current_model_idx = 0 # Сбрасываем на первую модель
                    else:
                        print(f"  [->] Пробуем следующую модель: {available_models[current_model_idx]}")
                        time.sleep(1)
                else:
                    print("  [!] Локальная модель зависла. Ждем 5 сек...")
                    time.sleep(5)
            else:
                print(f"  [!] Ошибка LLM: {e}")
                time.sleep(5)
                
    return None

def get_github_repos():
    print("Получаем список репозиториев...")
    url = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100"
    return requests.get(url).json()

def get_readme(repo_name):
    for branch in ["main", "master"]:
        url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/{branch}/README.md"
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
    return ""

def main():
    repos = get_github_repos()
    
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)
            
    tech_map = {}

    for repo in repos:
        repo_name = repo["name"]
        
        if repo_name in cache:
            print(f"[~] {repo_name} (из кэша)")
            skills = cache[repo_name]
        else:
            print(f"[+] Анализируем: {repo_name}...")
            description = repo.get("description", "") or "Без описания"
            language = repo.get("language", "") or "Не указан"
            readme = get_readme(repo_name)
            
            context = f"Репозиторий: {repo_name}. Язык: {language}. Описание: {description}.\n"
            if readme:
                context += readme[:2500]

            prompt = f"""
            Тщательно проанализируй текст и извлеки ВСЕ IT-технологии.
            Верни строго JSON: {{"skills": ["Python", "FastAPI", "Docker"]}}
            Контекст: {context}
            """
            
            res = safe_llm_call(prompt)
            skills = []
            if res:
                try:
                    json_match = re.search(r'\{.*\}', res, re.DOTALL)
                    if json_match:
                        skills = json.loads(json_match.group(0)).get("skills", [])
                except Exception as e:
                    print(f"  Ошибка парсинга: {e}")
            
            cache[repo_name] = skills
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)
            time.sleep(1)

        for skill in skills:
            skill_name = skill.strip()
            if skill_name not in tech_map:
                tech_map[skill_name] = []
            if repo_name not in tech_map[skill_name]:
                tech_map[skill_name].append(repo_name)

    print(f"\nВсего найдено технологий: {len(tech_map)}")
    
    for tech, repo_list in tech_map.items():
        slug = slugify(tech)
        existing_filepath = None
        for root, _, files in os.walk("docs"):
            if f"{slug}.md" in files:
                existing_filepath = os.path.join(root, f"{slug}.md")
                break
        
        if existing_filepath:
            with open(existing_filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            links_md = ""
            for repo in repo_list:
                link = f"- [{repo}](https://github.com/{GITHUB_USER}/{repo})"
                if link not in content:
                    links_md += f"{link}\n"
            
            if links_md:
                if "## Проекты" not in content:
                    content += f"\n## Проекты\n{links_md}"
                else:
                    content = content.replace("## Проекты\n", f"## Проекты\n{links_md}")
                with open(existing_filepath, "w", encoding="utf-8") as f:
                    f.write(content)
        else:
            print(f"  [+] Генерируем статью: {tech}...")
            prompt = f"""
            Ты база знаний. Сгенерируй статью по технологии: {tech}.
            1. Категория из: "llms", "frameworks", "databases", "concepts", "tools", "languages", "other".
            2. Markdown с разделами: Определение, Зачем нужно, Пример.
            Верни JSON: {{"category": "...", "markdown": "..."}}
            """
            res = safe_llm_call(prompt)
            if res:
                try:
                    json_match = re.search(r'\{.*\}', res, re.DOTALL)
                    if json_match:
                        data = json.loads(json_match.group(0))
                        category = data.get("category", "other")
                        markdown = data.get("markdown", "")
                        
                        folder_path = f"docs/{category}"
                        os.makedirs(folder_path, exist_ok=True)
                        
                        markdown += f"\n\n## Проекты\n"
                        for repo in repo_list:
                            markdown += f"- [{repo}](https://github.com/{GITHUB_USER}/{repo})\n"
                            
                        with open(f"{folder_path}/{slug}.md", "w", encoding="utf-8") as f:
                            f.write(f"# {tech}\n\n{markdown}")
                except Exception as e:
                    print(f"  Ошибка: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()