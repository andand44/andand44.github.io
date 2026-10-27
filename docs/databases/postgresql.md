# PostgreSQL

# PostgreSQL

## Определение
PostgreSQL — это свободная объектно-реляционная система управления базами данных (СУБД). Она сочетает в себе традиционные реляционные возможности и поддержку объектно-ориентированных концепций: наследование таблиц, пользовательские типы данных, функции на разных языках (PL/pgSQL, Python, JavaScript и др.), а также расширения вроде PostGIS для работы с геоданными.

## Зачем нужно
PostgreSQL используют, когда требуется надёжное, масштабируемое и стандартизированное хранилище данных с богатым функционалом:
- **ACID-совместимость** и транзакционная целостность.
- Поддержка сложных SQL-запросов, оконных функций, CTE и полнотекстового поиска.
- Гибкая работа с полуструктурированными данными через типы `JSON`/`JSONB`.
- Расширяемость: можно добавлять собственные типы, операторы, индексы и расширения.
- Активное сообщество, открытая лицензия и кроссплатформенность.

## Пример
Ниже приведён пример создания таблицы, вставки данных и выборки с использованием SQL в PostgreSQL:

```sql
-- Создание таблицы пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Вставка данных
INSERT INTO users (name, email, metadata) VALUES
('Alice', 'alice@example.com', '{"role": "admin", "active": true}'),
('Bob', 'bob@example.com', '{"role": "user", "active": true}');

-- Выборка активных администраторов за последнюю неделю
SELECT id, name, email, metadata
FROM users
WHERE metadata->>'role' = 'admin'
  AND created_at >= now() - INTERVAL '7 days'
ORDER BY created_at DESC;
```

## Проекты
- [ollama-agents](https://github.com/andand44/ollama-agents)
