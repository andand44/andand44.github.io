# Qdrant

## Определение
Qdrant — это высокопроизводительная векторная база данных (vector database) и система для поиска по сходству (similarity search) с открытым исходным кодом. Написана на языке Rust и предназначена для эффективного хранения, индексации и поиска высокоразмерных векторов (эмбеддингов), которые генерируются нейронными сетями. Qdrant предоставляет удобный API и поддерживает расширенную фильтрацию по метаданным (payload).

## Зачем нужно
С развитием машинного обучения и больших языковых моделей (LLM) возникла необходимость в эффективной работе с неструктурированными данными (тексты, изображения, аудио), преобразованными в векторные представления. Qdrant используется для решения следующих задач:
- **Семантический поиск:** поиск информации по смыслу, а не по точному совпадению ключевых слов.
- **RAG (Retrieval-Augmented Generation):** предоставление релевантного контекста для LLM, чтобы снизить количество галлюцинаций и дать моделям доступ к актуальным или приватным базам знаний.
- **Рекомендательные системы:** поиск похожих товаров, контента или пользователей на основе их векторных профилей.
- **Поиск дубликатов и аномалий:** быстрое выявление похожих или выбивающихся из общей картины объектов.

## Пример
Пример использования Qdrant на Python с помощью официального клиента для создания коллекции, добавления векторов и выполнения поиска:

```python
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

# Инициализация клиента (в оперативной памяти для примера)
client = QdrantClient(":memory:")

# Создание коллекции для хранения векторов размерностью 4
client.create_collection(
    collection_name="example_collection",
    vectors_config=VectorParams(size=4, distance=Distance.COSINE),
)

# Добавление точек (векторов с полезной нагрузкой)
client.upsert(
    collection_name="example_collection",
    points=[
        PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}),
        PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}),
        PointStruct(id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}),
    ]
)

# Поиск ближайших векторов к заданному запросу
search_result = client.search(
    collection_name="example_collection",
    query_vector=[0.2, 0.1, 0.9, 0.7],
    limit=2
)

# Вывод результатов
for result in search_result:
    print(f"ID: {result.id}, Score: {result.score}, City: {result.payload['city']}")
```

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
- [ollama-agents](https://github.com/andand44/ollama-agents)
