import os
import sys
import json
import re
from slugify import slugify # <-- Новая библиотека
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(base_url="https://api.orcarouter.ai/v1", api_key=os.getenv("LLM_API_KEY"))

def process_term(term_name, raw_description=""):
    # 1. Загружаем твои реальные навыки
    my_skills = []
    if os.path.exists("my_skills.json"):
        with open("my_skills.json", "r", encoding="utf-8") as f:
            my_skills = json.load(f)
            
    # 2. Проверяем, есть ли термин в твоем опыте (простой поиск по подстроке)
    is_known = any(term_name.lower() in skill.lower() or skill.lower() in term_name.lower() for skill in my_skills)
    
    if not is_known:
        print(f"⚠️ Внимание! Термина '{term_name}' нет в ваших проектах на GitHub.")
        user_input = input("Вы точно с ним работали? (y/n): ")
        if user_input.lower() != 'y':
            print("Отмена добавления.")
            return

    print(f"Проверяем и генерируем статью для '{term_name}'...")
    
    desc_prompt = f"Описание от пользователя: {raw_description}" if raw_description else "Описание отсутствует. Сгенерируй статью."
    
    prompt = f"""
    Ты база знаний разработчика. Напиши статью для вики.
    Термин: {term_name}
    {desc_prompt}
    
    Верни ответ СТРОГО в формате JSON:
    {{
        "category": "llms, frameworks, databases, concepts, tools или other",
        "markdown": "текст статьи с разделами Определение, Зачем нужно, Пример"
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-v4-flash-free",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        data = json.loads(response.choices[0].message.content)
        category = data.get("category", "other")
        markdown_text = data.get("markdown", "")
        
        # 3. ИСПОЛЬЗУЕМ SLUGIFY ДЛЯ ИМЕНИ ФАЙЛА (исправляет баг с ______.md)
        safe_filename = slugify(term_name) 
        folder_path = f"docs/{category}"
        filepath = f"{folder_path}/{safe_filename}.md"
        
        if os.path.exists(filepath):
            print(f"⚠️ Термин '{term_name}' уже существует в категории {category}!")
            return
            
        os.makedirs(folder_path, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {term_name}\n\n{markdown_text}")
            
        print(f"✅ Успех! Термин сохранен в {filepath}")
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python add_term.py 'Название' ['Описание']")
    else:
        term = sys.argv[1]
        desc = sys.argv[2] if len(sys.argv) > 2 else ""
        process_term(term, desc)