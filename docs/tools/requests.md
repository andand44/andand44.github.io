# requests

# Requests

## Определение
`requests` — это популярная библиотека для языка Python, которая предоставляет простой и удобный интерфейс для отправки HTTP-запросов. Она позволяет взаимодействовать с веб-сервисами и API, выполнять методы GET, POST, PUT, DELETE и другие, работать с заголовками, параметрами, куками, сессиями и аутентификацией. Библиотека не входит в стандартную библиотеку Python и устанавливается через пакетный менеджер pip.

## Зачем нужно
- Упрощает работу с HTTP по сравнению со встроенным модулем `urllib`.
- Позволяет быстро интегрироваться с REST API, получать данные в формате JSON, отправлять формы и файлы.
- Поддерживает сессии (`Session`), сохраняющие куки и заголовки между запросами.
- Автоматически обрабатывает кодировки, редиректы, таймауты и SSL.
- Широко используется в веб-скрапинге, тестировании, микросервисах и автоматизации.

## Пример
Установка:

```bash
pip install requests
```

Пример GET- и POST-запросов:

```python
import requests

# GET-запрос с параметрами
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    timeout=10
)
response.raise_for_status()
data = response.json()
print(data['items'][0]['full_name'])

# POST-запрос с JSON-телом
payload = {'name': 'Alice', 'job': 'Engineer'}
response = requests.post(
    'https://reqres.in/api/users',
    json=payload,
    headers={'Authorization': 'Bearer token'},
    timeout=10
)
print(response.status_code)
print(response.json())
```

В этом примере мы получаем список репозиториев с GitHub и создаём пользователя через тестовый API. Метод `response.json()` автоматически декодирует JSON-ответ, а `raise_for_status()` помогает обрабатывать ошибки HTTP.

## Проекты
- [ollama-agents](https://github.com/andand44/ollama-agents)
