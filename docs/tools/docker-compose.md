# Docker Compose

## Определение

**Docker Compose** — это инструмент командной строки (CLI) и формат файла для определения и запуска многоконтейнерных приложений на базе Docker. Конфигурация описывается в YAML-файле (обычно `docker-compose.yml`), где объявляются **сервисы** (контейнеры), сети, тома и зависимости между ними. После этого весь стек поднимается одной командой, например `docker compose up`.

Compose может работать как отдельная утилита `docker-compose` (Compose V1) или как подкоманда Docker CLI — `docker compose` (Compose V2, рекомендуемый вариант). Он не заменяет полноценные оркестраторы уровня Kubernetes, но отлично подходит для локальной разработки, тестирования и несложных развёртываний.

## Зачем нужно

Docker Compose решает проблему ручного запуска и связывания множества контейнеров. Основные задачи и преимущества:

- **Описание инфраструктуры как код (IaC)** — вся конфигурация хранится в одном файле и версионируется в Git.
- **Быстрый запуск окружения** — разработчик поднимает весь стек одной командой (`docker compose up`).
- **Управление зависимостями** — можно указать порядок запуска сервисов через `depends_on`.
- **Изоляция и повторяемость** — одинаковое окружение на машинах разработчиков, в CI и на staging.
- **Сети и тома** — Compose автоматически создаёт общую сеть для сервисов и управляет постоянными данными через volumes.
- **Масштабирование** — можно запустить несколько экземпляров сервиса: `docker compose up --scale worker=3`.
- **Переменные окружения и секреты** — удобная передача конфигурации в контейнеры.

## Пример

Файл `docker-compose.yml` для простого веб-приложения с базой данных PostgreSQL:

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    depends_on:
      - db
    networks:
      - app-network

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

volumes:
  db-data:
```

Запуск стека:

```bash
# Поднять все сервисы в фоновом режиме
docker compose up -d

# Посмотреть логи
docker compose logs -f

# Остановить и удалить контейнеры, сети
docker compose down
```

В этом примере Compose создаст два сервиса (`web` и `db`), изолированную сеть `app-network` и именованный том `db-data` для хранения данных PostgreSQL. Приложение будет доступно по адресу `http://localhost:8080`.

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
