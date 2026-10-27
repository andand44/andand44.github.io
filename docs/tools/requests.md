# requests

## Определение

`requests` — это библиотека для Python, которая упрощает отправку HTTP-запросов. Она позволяет взаимодействовать с веб-ресурсами и API, поддерживает методы GET, POST, PUT, DELETE, работу с заголовками, параметрами, cookies, сессиями и SSL.

## Зачем нужно

- Упрощает интеграцию с REST API и веб-сервисами.
- Автоматически обрабатывает JSON, редиректы, кодировки и таймауты.
- Позволяет управлять сессиями, куками и авторизацией.
- Широко применяется в парсинге, автоматизации, тестировании и микросервисах.

## Пример

Установка:

```bash
pip install requests
```

Пример использования:

```python
import requests

# GET-запрос
response = requests.get('https://api.github.com/user', headers={'Authorization': 'token YOUR_TOKEN'})
print(response.status_code)
print(response.json())

# POST-запрос
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.text)
```

## Проекты
- [ollama-agents](https://github.com/andand44/ollama-agents)
