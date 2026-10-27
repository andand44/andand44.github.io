# Qdrant

# Qdrant

## Определение
**Qdrant** — это высокопроизводительная векторная база данных (vector database) и система для поиска по сходству (similarity search) с открытым исходным кодом. Она написана на языке Rust и предназначена для хранения, индексации и поиска высокоразмерных векторов (эмбеддингов). Qdrant предоставляет удобный API, позволяющий эффективно работать с векторными данными, и поддерживает расширенную фильтрацию по дополнительным метаданным (payload).

## Зачем нужно
В эпоху машинного обучения и больших языковых моделей (LLM) традиционные базы данных плохо справляются с поиском по смыслу (семантическим сходством). Qdrant решает эту проблему и используется для:
- **Семантического поиска:** поиск документов или товаров, наиболее близких по смыслу к текстовому запросу.
- **RAG (Retrieval-Augmented Generation):** предоставление релевантного контекста большим языковым моделям для генерации более точных и обоснованных ответов без галлюцинаций.
- **Рекомендательных систем:** подбор контента, товаров или музыки на основе векторных представлений предпочтений пользователей.
- **Поиска похожих изображений, аудио или видео:** поиск дубликатов или визуально/аудиально похожего контента.

## Пример
Ниже приведен простой пример использования Qdrant на Python с помощью официального клиента для создания коллекции, добавления векторов и выполнения поиска:

```python
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

# Инициализация клиента (в памяти для примера)
client = QdrantClient(":memory:")

# Создание коллекции для векторов размерностью 4
client.create_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=4, distance=Distance.COSINE),
)

# Добавление точек (векторов с полезной нагрузкой)
client.upsert(
    collection_name="my_collection",
    points=[
        PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),
        PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}),
        PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}),
    ]
)

# Поиск 2 ближайших векторов к заданному запросу
search_result = client.search(
    collection_name="my_collection",
    query_vector=[0.2, 0.1, 0.9, 0.7],
    limit=2
)

for result in search_result:
    print(f"ID: {result.id}, Score: {result.score}, City: {result.payload['city']}")
```

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
- [ollama-agents](https://github.com/andand44/ollama-agents)
