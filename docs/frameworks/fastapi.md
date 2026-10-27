# FastAPI

### Определение

FastAPI — это современный, высокопроизводительный веб-фреймворк для создания API на языке Python (версии 3.7 и выше). Он основан на стандартных аннотациях типов Python, использует Starlette для асинхронной обработки запросов и Pydantic для валидации данных.

### Зачем нужно

FastAPI применяется для быстрой и эффективной разработки надежных REST API. Основные причины его использования:
- **Высокая производительность:** Благодаря поддержке асинхронности (ASGI), скорость работы сопоставима с Node.js и Go.
- **Автоматическая документация:** Фреймворк автоматически генерирует интерактивную документацию (Swagger UI и ReDoc) на основе написанного кода.
- **Валидация данных:** Встроенная мощная валидация и сериализация данных с помощью Pydantic.
- **Скорость разработки:** Минимизирует количество шаблонного кода и снижает количество ошибок за счет подсказок типов (type hints).

### Пример

Простейший пример приложения на FastAPI с использованием асинхронного эндпоинта:

```python
from fastapi import FastAPI
from pydantic import BaseModel

# Инициализация приложения
app = FastAPI()

# Модель данных для валидации
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# Базовый эндпоинт
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Эндпоинт с параметрами пути и запроса
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Эндпоинт для обновления данных (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

Чтобы запустить это приложение, достаточно сохранить код в файл `main.py` и выполнить команду `uvicorn main:app --reload` в терминале.

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
- [ollama-agents](https://github.com/andand44/ollama-agents)
