# pymysql

## Определение
PyMySQL — это чистая Python-библиотека (pure-Python) для взаимодействия с реляционными базами данных MySQL и совместимыми с ними (например, MariaDB). Она реализует протокол клиента MySQL на уровне Python и предоставляет DB-API 2.0 (PEP 249)-совместимый интерфейс для выполнения SQL-запросов, управления транзакциями и получения результатов. PyMySQL можно использовать как замену MySQLdb в проектах, где нежелательна сборка C-расширений.

## Зачем нужно
- Подключение приложений на Python к MySQL/MariaDB без установки дополнительных системных зависимостей и компиляции.
- Выполнение SQL-запросов: SELECT, INSERT, UPDATE, DELETE, вызов хранимых процедур.
- Управление транзакциями (commit/rollback) и курсорами.
- Совместимость с популярными ORM и фреймворками (например, SQLAlchemy, Django через соответствующие бэкенды).
- Подходит для скриптов, микросервисов, веб-приложений и ETL-процессов, где требуется работать с MySQL.

## Пример
Пример подключения к базе данных и выполнения простого запроса:

```python
import pymysql

# Установка соединения
connection = pymysql.connect(
    host='localhost',
    user='user',
    password='password',
    database='test_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Создание таблицы
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL
            )
        ''')

        # Вставка данных
        sql = 'INSERT INTO users (name, email) VALUES (%s, %s)'
        cursor.execute(sql, ('Alice', 'alice@example.com'))

    # Фиксация изменений
    connection.commit()

    with connection.cursor() as cursor:
        # Чтение данных
        cursor.execute('SELECT id, name, email FROM users')
        result = cursor.fetchall()
        for row in result:
            print(row)
finally:
    connection.close()
```

В примере используется параметризованный запрос (`%s`), что помогает защититься от SQL-инъекций. Курсор `DictCursor` возвращает строки в виде словарей.

## Проекты
- [modulbank-test](https://github.com/andand44/modulbank-test)
