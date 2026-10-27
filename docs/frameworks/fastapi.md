# FastAPI

## Определение

FastAPI — это современный, высокопроизводительный веб-фреймворк для создания API на языке Python (версии 3.7+). Он основан на стандартах OpenAPI и JSON Schema, использует асинхронность (ASGI) и аннотации типов Python для автоматической валидации данных, сериализации и генерации интерактивной документации (Swagger UI, ReDoc).

## Зачем нужно

FastAPI нужен для быстрой разработки надежных и масштабируемых HTTP API. Основные причины использования:

- **Высокая производительность**: сравнима с Node.js и Go благодаря ASGI-серверам (Uvicorn, Hypercorn).
- **Автоматическая документация**: генерирует OpenAPI-спецификацию и UI для тестирования endpoints из коробки.
- **Валидация данных**: использует Pydantic и подсказки типов, уменьшая количество ошибок и boilerplate-кода.
- **Асинхронность**: поддерживает `async`/`await` для эффективной обработки I/O-bound задач.
- **Удобство разработки**: минимум кода, автодополнение в IDE, строгая типизация.

## Пример

Простейшее приложение FastAPI с базовыми маршрутами:

```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get('/')
async def read_root():
    return {'message': 'Hello, FastAPI!'}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}

@app.post('/items/')
async def create_item(item: Item):
    return {'item_name': item.name, 'item_price': item.price}
```

Запуск приложения (например, через Uvicorn):

```bash
uvicorn main:app --reload
```

После запуска документация будет доступна по адресам `/docs` (Swagger UI) и `/redoc`.

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
- [ollama-agents](https://github.com/andand44/ollama-agents)
