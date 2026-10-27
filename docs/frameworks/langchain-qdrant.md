# LangChain-Qdrant

## Определение

**LangChain-Qdrant** — это интеграция фреймворка LangChain с векторной базой данных Qdrant. Данная связка позволяет использовать Qdrant в качестве надежного и высокопроизводительного хранилища векторов (vector store) в приложениях на базе больших языковых моделей (LLM), создаваемых с помощью LangChain. Она обеспечивает сохранение, индексацию и извлечение эмбеддингов (векторных представлений текста).

## Зачем нужно

Интеграция LangChain и Qdrant в первую очередь необходима для реализации архитектуры **Retrieval-Augmented Generation (RAG)**. Она решает ключевые проблемы LLM, такие как ограниченное контекстное окно и склонность к галлюцинациям.

С помощью этой технологии разработчики могут:
- Обучать LLM на собственных или актуальных данных без дорогостоящего файн-тюнинга.
- Осуществлять быстрый семантический поиск по огромным массивам неструктурированной информации.
- Создавать интеллектуальных чат-ботов, системы ответов на вопросы и рекомендательные сервисы, которые опираются на внешнюю базу знаний.

## Пример

Ниже приведен базовый пример на Python, демонстрирующий, как LangChain использует Qdrant для сохранения текстов и последующего поиска по ним:

```python
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

# Инициализация клиента Qdrant (в оперативной памяти для примера)
client = QdrantClient(":memory:")

# Создание коллекции для векторов
client.create_collection(
    collection_name="knowledge_base",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
)

# Инициализация модели для создания эмбеддингов
embeddings = OpenAIEmbeddings()

# Создание векторного хранилища в LangChain
vectorstore = Qdrant(
    client=client, 
    collection_name="knowledge_base", 
    embeddings=embeddings
)

# Добавление документов в базу
texts = [
    "LangChain — это мощный фреймворк для разработки приложений с LLM.",
    "Qdrant — это векторная база данных, оптимизированная для поиска по сходству."
]
vectorstore.add_texts(texts)

# Поиск релевантной информации
query = "Что такое Qdrant?"
found_docs = vectorstore.similarity_search(query)

print(found_docs[0].page_content)
# Вывод: Qdrant — это векторная база данных, оптимизированная для поиска по сходству.
```

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
