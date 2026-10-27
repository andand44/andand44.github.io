# LangChain-Qdrant

### Определение

LangChain-Qdrant — это интеграция векторной базы данных Qdrant с фреймворком LangChain. Данная связка позволяет использовать Qdrant в качестве векторного хранилища (vector store) для эффективного семантического поиска и извлечения релевантной информации, которая затем передается в большие языковые модели (LLM) для генерации ответов.

### Зачем нужно

Интеграция LangChain-Qdrant используется для создания приложений на базе архитектуры Retrieval-Augmented Generation (RAG). Основные цели использования:

- **Семантический поиск:** Быстрое нахождение документов, наиболее близких по смыслу к запросу пользователя, на основе векторных представлений (эмбеддингов).
- **Долговременная память:** Обеспечение LLM доступом к внешним базам знаний, что позволяет модели отвечать на вопросы, выходящие за рамки ее обучающих данных.
- **Снижение галлюцинаций:** Предоставление модели точного контекста из базы данных повышает фактическую точность и актуальность генерируемых ответов.
- **Масштабируемость:** Qdrant справляется с большими объемами данных и высокой нагрузкой, что делает его надежным решением для продакшен-систем.

### Пример

Пример инициализации и использования Qdrant в качестве векторного хранилища в LangChain на языке Python:

```python
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient

# Инициализация клиента Qdrant
client = QdrantClient(url="http://localhost:6333")

# Инициализация модели для создания эмбеддингов
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Создание векторного хранилища на базе Qdrant
vector_store = QdrantVectorStore(
    client=client,
    collection_name="my_collection",
    embedding=embeddings,
)

# Добавление текстов в базу данных
texts = [
    "LangChain — это фреймворк для разработки приложений с использованием LLM.",
    "Qdrant — это высокопроизводительная векторная база данных."
]
vector_store.add_texts(texts)

# Поиск релевантных документов по запросу
query = "Что такое LangChain?"
found_docs = vector_store.similarity_search(query)

for doc in found_docs:
    print(doc.page_content)
```

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
