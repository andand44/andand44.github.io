# OpenTelemetry

## Определение

OpenTelemetry (сокращённо OTel) — это открытый стандарт и набор инструментов для сбора, генерации и экспорта телеметрии: распределённых трейсов, метрик и логов. Проект объединил усилия OpenTracing и OpenCensus и развивается под эгидой CNCF. OpenTelemetry предоставляет API, SDK, агенты и коллектор (OpenTelemetry Collector), но не занимается хранением или визуализацией данных: вместо этого он передаёт их в совместимые бэкенды, такие как Jaeger, Prometheus, Grafana, Zipkin или коммерческие SaaS-платформы.

## Зачем нужно

- **Устранение фрагментации.** Раньше для метрик, трейсов и логов использовались разные библиотеки и форматы. OpenTelemetry предлагает единый подход.
- **Вендорная независимость.** Инструментирование кода не привязано к конкретному вендору: бэкенд можно заменить без переписывания приложения.
- **Связность телеметрии.** Общий контекст трейсинга позволяет связывать логи, метрики и спаны, что упрощает отладку микросервисов.
- **Автоматическая инструментация.** Готовые интеграции для популярных фреймворков, HTTP-клиентов, баз данных и брокеров сообщений ускоряют внедрение.
- **Стандартизация observability.** Единый пайплайн упрощает эксплуатацию в Kubernetes и CI/CD, снижает стоимость поддержки мониторинга.

## Пример

Пример ручного инструментирования Python-приложения с помощью OpenTelemetry SDK и вывода трейсов в консоль:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.sdk.resources import Resource

# Инициализация провайдера трейсов
resource = Resource.create({'service.name': 'my-service'})
provider = TracerProvider(resource=resource)
processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

# Создание спана
with tracer.start_as_current_span('main-operation') as span:
    span.set_attribute('operation.value', 42)
    print('Выполняется операция...')
    # Вложенная операция
    with tracer.start_as_current_span('child-operation'):
        print('Дочерняя операция')
```

Для автоматического сбора телеметрии можно использовать обёртку `opentelemetry-instrument`:

```bash
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install
OTEL_SERVICE_NAME=my-service OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 opentelemetry-instrument python app.py
```

В результате приложение начнёт отправлять трейсы и метрики по протоколу OTLP в коллектор, откуда они могут быть направлены в систему хранения и визуализации.

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
