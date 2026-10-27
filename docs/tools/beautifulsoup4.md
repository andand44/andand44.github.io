# BeautifulSoup4

# BeautifulSoup4

## Определение

BeautifulSoup4 (или bs4) — это библиотека для языка Python, предназначенная для парсинга (разбора) документов HTML и XML. Она преобразует разметку в удобное дерево объектов и предоставляет простой API для поиска, извлечения и изменения данных. BeautifulSoup4 может работать с разными бэкендами-парсерами, например `html.parser`, `lxml` или `html5lib`.

## Зачем нужно

- **Веб-скрапинг**: извлечение текста, ссылок, изображений, таблиц и других данных с веб-страниц.
- **Обработка неструктурированных данных**: превращение «сырого» HTML в структурированную информацию (например, в JSON или CSV).
- **Устойчивость к ошибкам разметки**: библиотека корректно обрабатывает незакрытые теги и некорректный HTML, восстанавливая структуру документа.
- **Автоматизация**: сбор данных с сайтов, у которых нет публичного API, для аналитики, мониторинга цен, агрегации контента и т.д.
- **Совместимость**: легко комбинируется с `requests` для загрузки страниц и с `pandas` для анализа полученных таблиц.

## Пример

Установка библиотеки и зависимостей:

```bash
pip install beautifulsoup4 requests
```

Пример парсинга страницы: получаем заголовок и список ссылок.

```python
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
response.raise_for_status()

# Создаем объект BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Заголовок страницы
print('Title:', soup.title.string)

# Все ссылки на странице
for link in soup.find_all('a'):
    href = link.get('href')
    text = link.get_text(strip=True)
    print(f'{text}: {href}')

# Первый параграф через CSS-селектор
first_paragraph = soup.select_one('p')
if first_paragraph:
    print('First paragraph:', first_paragraph.get_text(strip=True))
```

## Проекты
- [ollama-agents](https://github.com/andand44/ollama-agents)
