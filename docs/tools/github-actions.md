# GitHub Actions

## Определение

GitHub Actions — это платформа для автоматизации рабочих процессов (CI/CD) непосредственно в репозитории GitHub. Она позволяет описывать сценарии сборки, тестирования и развёртывания проекта с помощью YAML-файлов, которые хранятся в каталоге `.github/workflows`. Workflow запускается по триггерам: push, pull request, расписание и др.

## Зачем нужно

- Автоматизация рутинных задач: сборка, тесты, линтеры, публикация пакетов.
- Быстрая обратная связь при изменениях кода.
- Единая инфраструктура рядом с кодом, без отдельного CI-сервера.
- Масштабируемость на разные ОС (Linux, Windows, macOS) и окружения.
- Интеграция с экосистемой GitHub и маркетплейсом готовых действий.

## Пример

Простейший workflow для Node.js проекта, который при пуше в ветку `main` устанавливает зависимости и запускает тесты:

```yaml
name: Node.js CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm test
```

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
