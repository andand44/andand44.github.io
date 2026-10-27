# Pytest

## Определение

Pytest — это популярный фреймворк для тестирования на языке Python. Он позволяет писать компактные и выразительные тесты, используя обычный оператор `assert`, и предоставляет мощные возможности: фикстуры (fixtures), параметризацию, маркировку тестов и систему плагинов. Pytest подходит как для модульных (unit) тестов, так и для функционального и интеграционного тестирования.

## Зачем нужно

- **Минимум шаблонного кода**: тесты представляют собой обычные функции, начинающиеся с `test_`, что упрощает их чтение и поддержку.
- **Фикстуры**: механизм подготовки и очистки окружения (setup/teardown) с разными областями видимости (function, class, module, session).
- **Параметризация**: декоратор `@pytest.mark.parametrize` позволяет запускать один и тот же тест с разными входными данными.
- **Подробные отчёты**: при падении теста Pytest показывает значения переменных и контекст, что ускоряет отладку.
- **Плагины и интеграции**: огромная экосистема (`pytest-django`, `pytest-asyncio`, `pytest-cov`, `pytest-xdist` и др.) и лёгкая встройка в CI/CD.
- **Гибкий запуск**: можно запускать все тесты, отдельный файл, класс или конкретный тест, а также использовать маркеры (`@pytest.mark.slow`) для выборочного прогона.

## Пример

Установка:

```bash
pip install pytest
```

Пример тестируемого кода и тестов в файле `test_calc.py`:

```python
import pytest

def inc(x):
    return x + 1

@pytest.fixture
def base_value():
    return 10

def test_inc_simple():
    assert inc(3) == 4

def test_inc_with_fixture(base_value):
    assert inc(base_value) == 11

@pytest.mark.parametrize('value, expected', [(1, 2), (5, 6), (-1, 0)])
def test_inc_param(value, expected):
    assert inc(value) == expected
```

Запуск тестов:

```bash
pytest -v
```

Pytest автоматически найдёт файлы, начинающиеся с `test_`, выполнит функции `test_*` и выведет подробный отчёт о результатах.

## Проекты
- [modulbank-test](https://github.com/andand44/modulbank-test)
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
- [ollama-agents](https://github.com/andand44/ollama-agents)
