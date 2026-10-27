# Docker Compose

# Docker Compose

## Определение
Docker Compose — это инструмент для определения и запуска многоконтейнерных приложений Docker. С помощью YAML-файла (обычно `docker-compose.yml`) вы описываете сервисы, сети и тома, а затем одной командой создаёте и запускаете все контейнеры.

## Зачем нужно
- Упрощает локальную разработку и тестирование: поднимает всю инфраструктуру (БД, кэш, бэкенд, фронтенд) одной командой.
- Декларативность: вся конфигурация хранится в файле, её легко версионировать в Git.
- Изоляция окружений: можно описывать разные сервисы и зависимости для dev/stage/prod.
- Автоматическое создание сетей: контейнеры одного compose-проекта видят друг друга по именам сервисов.
- Управление жизненным циклом: команды `up`, `down`, `logs`, `ps`, `exec` и другие.

## Пример
Пример `docker-compose.yml` для веб-приложения и базы данных PostgreSQL:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - "DATABASE_URL=postgresql://user:password@db:5432/mydb"
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Запуск в фоновом режиме:

```bash
docker compose up -d
```

Остановка и удаление контейнеров:

```bash
docker compose down
```

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
