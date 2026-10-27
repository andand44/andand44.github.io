import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import re

load_dotenv()

# Настройка клиента OrcaRouter (OpenAI-совместимый)
client = OpenAI(
    base_url="https://api.orcarouter.ai/v1",
    api_key=os.getenv("LLM_API_KEY")
)

def process_term(term_name, raw_description):
    print(f"Отправляем '{term_name}' на проверку нейросети...")
    
    prompt = f"""
    Ты Senior AI Engineer. Пользователь добавил новый термин в свою базу знаний.
    Проверь его на фактические ошибки, исправь стилистику и дополни полезными деталями.
    
    Термин: {term_name}
    Описание: {raw_description}
    
    Верни ответ СТРОГО в формате Markdown. Без лишних вступлений.
    Используй заголовок второго уровня (##) для названия.
    Сделай разделы: Определение, Зачем нужно (если применимо), Пример использования.
    """
    
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-v4-flash-free", # <-- ИЗМЕНИТЕ ЭТУ СТРОКУ
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        
        final_text = response.choices[0].message.content
        
        # Очищаем имя файла от лишних символов
        safe_filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', term_name.lower())
        filepath = f"docs/{safe_filename}.md"
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(final_text)
            
        print(f"Успех! Термин сохранен в {filepath}")
        
    except Exception as e:
        print(f"Ошибка при обращении к LLM: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python add_term.py 'Название термина' 'Твое сырое описание'")
    else:
        process_term(sys.argv[1], sys.argv[2])