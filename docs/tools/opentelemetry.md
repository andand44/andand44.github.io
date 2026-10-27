# OpenTelemetry

# OpenTelemetry

## Определение

OpenTelemetry (OTel) — это открытый стандарт и набор инструментов (API, SDK, библиотеки и агент/коллектор) для инструментирования приложений и сбора телеметрии: трассировок (traces), метрик (metrics) и логов (logs). Проект развивается под эгидой CNCF и призван унифицировать способы генерации, сбора и экспорта данных наблюдаемости (observability) в распределённых системах.

Основные компоненты:

- **API** — интерфейсы для создания спанов, метрик и логов в коде.
- **SDK** — реализации API для конкретных языков с поддержкой процессоров и экспортёров.
- **OpenTelemetry Collector** — отдельный сервис для приёма, обработки, фильтрации и маршрутизации телеметрии.
- **Экспортёры (exporters)** — модули для отправки данных в бэкенды (Jaeger, Prometheus, Grafana, Datadog, OTLP и др.).
- **Семантические соглашения** — единые имена атрибутов и ресурсов для совместимости данных.

## Зачем нужно

- **Единый стандарт.** Раньше для трассировки, метрик и логов использовались разные, часто несовместимые библиотеки. OpenTelemetry объединяет их в одном подходе.
- **Независимость от вендора.** Инструментирование остаётся прежним при смене системы мониторинга: достаточно поменять экспортёр или конфигурацию Collector.
- **Сквозная трассировка.** Позволяет проследить путь запроса через микросервисы, найти узкие места и причины ошибок.
- **Корреляция сигналов.** Трейсы, метрики и логи связываются общими идентификаторами (trace_id, span_id), что ускоряет диагностику.
- **Автоматическое инструментирование.** Для популярных языков и фреймворков есть готовые библиотеки, которые подключаются без изменения кода.
- **Гибкая обработка.** Collector умеет обогащать, сэмплировать, фильтровать и преобразовывать данные перед отправкой.

## Пример

Ниже показан пример ручного инструментирования Python-приложения: создаётся трейс с вложенным спаном, а результат выводится в консоль.

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.sdk.resources import Resource

# Настраиваем провайдер трейсов
resource = Resource.create({"service.name": "my-service"})
provider = TracerProvider(resource=resource)
processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("main-operation") as span:
    span.set_attribute("example.attribute", "value")
    print("Выполняется работа...")
    with tracer.start_as_current_span("child-operation"):
        print("Вложенная операция")
```

В продакшене вместо `ConsoleSpanExporter` обычно используют `OTLPSpanExporter`, который отправляет данные по протоколу OTLP в OpenTelemetry Collector или напрямую в бэкенд наблюдаемости, например Jaeger.

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
