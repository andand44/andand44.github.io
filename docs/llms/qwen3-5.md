# qwen3.5

## Определение

**Qwen 3.5** — это перспективная (ожидаемая) итерация в семействе больших языковых моделей (LLM) Qwen (Tongyi Qianwen), разрабатываемых компанией Alibaba Cloud. Модели семейства Qwen зарекомендовали себя как одни из самых мощных ИИ-решений на рынке. Версия 3.5, вероятно, предложит улучшенную архитектуру (в том числе с использованием подхода Mixture of Experts — MoE), расширенное контекстное окно и передовые способности к сложным рассуждениям (reasoning).

## Зачем нужно

Развитие моделей уровня Qwen 3.5 необходимо для решения ряда актуальных задач в области искусственного интеллекта:

- **Сложные рассуждения (Reasoning):** Повышение способности модели решать многошаговые логические, математические и программные задачи, составляя конкуренцию лучшим проприетарным моделям.
- **Мультимодальность:** Углубленная интеграция обработки текста, изображений, аудио и видео, что позволяет создавать более сложных и универсальных ИИ-ассистентов.
- **Эффективность и масштабируемость:** Оптимизация архитектуры для снижения вычислительных затрат при сохранении высокой производительности, что делает развертывание моделей более доступным для бизнеса и локального использования.
- **Развитие Open Source:** Поддержание тренда на выпуск мощных открытых моделей, что стимулирует глобальное сообщество разработчиков и ускоряет технологические инновации.

## Пример

Поскольку точные спецификации Qwen 3.5 могут отличаться, рассмотрим гипотетический пример использования модели через библиотеку `transformers` от Hugging Face для генерации программного кода (по аналогии с текущими версиями Qwen):

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Предполагаемое название модели
model_name = "Qwen/Qwen3.5-7B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# Формирование запроса
prompt = "Напиши функцию на Python для быстрой сортировки массива."
messages = [
    {"role": "system", "content": "Ты полезный ИИ-ассистент, эксперт в программировании."},
    {"role": "user", "content": prompt}
]

# Применение чат-шаблона
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Генерация ответа
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=256
)

# Извлечение только сгенерированной части ответа
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
