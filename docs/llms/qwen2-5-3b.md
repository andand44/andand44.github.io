# Qwen2.5:3B

## Определение

**Qwen2.5:3B** — это компактная большая языковая модель (LLM) с 3 миллиардами параметров, разработанная компанией Alibaba Cloud. Она входит в семейство моделей Qwen2.5 и представляет собой открытую (open-source) нейросеть, обученную на обширном массиве данных. Модель оптимизирована для решения широкого спектра задач: от генерации текста, перевода и суммаризации до написания кода и решения математических задач. Она поддерживает мультиязычность (включая русский и английский) и обладает расширенным контекстным окном для обработки длинных диалогов и документов.

## Зачем нужно

Главная цель создания Qwen2.5:3B — предоставить мощный инструмент искусственного интеллекта, который сочетает в себе высокую производительность и низкие требования к аппаратному обеспечению. Благодаря относительно небольшому количеству параметров (3B), модель может эффективно запускаться локально на потребительских видеокартах (GPU) или даже на CPU. Это делает её идеальным выбором для:
- **Локального развертывания:** Обеспечение конфиденциальности данных без необходимости отправки запросов в облако.
- **Экономии ресурсов:** Снижение затрат на аренду дорогих серверов с мощными GPU.
- **Кастомизации:** Возможность быстрой тонкой настройки (fine-tuning) под узкоспециализированные бизнес-задачи.
- **Создания чат-ботов и ассистентов:** Обеспечение быстрого отклика при генерации ответов в реальном времени.

## Пример

Ниже приведен пример использования модели `Qwen2.5-3B-Instruct` на Python с помощью библиотеки `transformers` для генерации ответа на запрос пользователя:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Указываем название модели в Hugging Face
model_name = "Qwen/Qwen2.5-3B-Instruct"

# Загружаем модель и токенизатор
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Формируем запрос
prompt = "Напиши короткое стихотворение про программирование."
messages = [
    {"role": "system", "content": "Ты полезный ИИ-ассистент."},
    {"role": "user", "content": prompt}
]

# Применяем шаблон чата
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Генерируем ответ
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=256
)

# Извлекаем только сгенерированный текст (отсекаем ввод)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

# Декодируем и выводим результат
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

## Проекты
- [ollama-agents](https://github.com/andand44/ollama-agents)
