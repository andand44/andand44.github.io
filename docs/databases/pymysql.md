# pymysql

# PyMySQL

## Определение
**PyMySQL** — это библиотека на языке Python, представляющая собой чистую реализацию клиента для работы с базами данных MySQL. Она позволяет приложениям на Python подключаться к серверу MySQL, выполнять SQL-запросы и управлять данными. В отличие от других драйверов (например, `mysqlclient`), PyMySQL полностью написан на чистом Python и не требует компиляции C-расширений.

## Зачем нужно
PyMySQL необходим для интеграции реляционных баз данных MySQL в экосистему Python. Основные причины использования:
- **Взаимодействие с БД:** Обеспечивает выполнение всех стандартных операций (CRUD) с помощью SQL-запросов.
- **Простота установки:** Отсутствие зависимостей от системных библиотек делает установку через `pip` быстрой и беспроблемной на любой ОС.
- **Совместимость с DB-API 2.0:** Соблюдение стандарта Python Database API позволяет легко переключаться между разными базами данных.
- **Замена MySQLdb:** Часто используется как прозрачная замена (drop-in replacement) для `MySQLdb` в проектах, где важна портативность и отсутствие компиляции.

## Пример
Пример базового использования PyMySQL для подключения к базе данных, создания таблицы, добавления записи и чтения данных:

```python
import pymysql

# Подключение к базе данных
connection = pymysql.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='test_db',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Создание таблицы
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                position VARCHAR(100)
            )
        """)
        
        # Вставка данных
        sql = "INSERT INTO employees (name, position) VALUES (%s, %s)"
        cursor.execute(sql, ('John Doe', 'Developer'))
    
    # Сохранение изменений
    connection.commit()

    with connection.cursor() as cursor:
        # Чтение данных
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        for row in result:
            print(row)

finally:
    # Закрытие соединения
    connection.close()
```

## Проекты
- [modulbank-test](https://github.com/andand44/modulbank-test)
