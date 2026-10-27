import os
import json
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(base_url="https://api.orcarouter.ai/v1", api_key=os.getenv("LLM_API_KEY"))

GITHUB_USER = "andand44"
REPOS = ["enterprise-rag-service", "ollama-agents", "ai-second-brain"]

def fetch_readme(repo_name):
    # Пытаемся скачать README.md
    for branch in ["main", "master"]:
        url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/{branch}/README.md"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    return ""

def extract_skills_from_readmes():
    all_text = ""
    for repo in REPOS:
        print(f"Читаем {repo}...")
        readme = fetch_readme(repo)
        if readme:
            all_text += f"\n--- Проект: {repo} ---\n{readme[:3000]}\n" # Берем первые 3000 символов

    print("Отправляем текст нейросети для извлечения технологий...")
    prompt = f"""
    Проанализируй текст из README проектов разработчика. 
    Выдели список IT-технологий, инструментов и библиотек, с которыми он точно работал (например: Python, FastAPI, Docker, Qdrant, LangChain).
    Верни ответ СТРОГО в формате JSON: {{"skills": ["Python", "FastAPI", "Docker"]}}
    Не добавляй то, чего нет в тексте.
    
    Текст:
    {all_text}
    """
    
    response = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash-free",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    
    data = json.loads(response.choices[0].message.content)
    skills = data.get("skills", [])
    
    with open("my_skills.json", "w", encoding="utf-8") as f:
        json.dump(skills, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Найдено и сохранено {len(skills)} технологий в my_skills.json:")
    print(", ".join(skills))

if __name__ == "__main__":
    extract_skills_from_readmes()