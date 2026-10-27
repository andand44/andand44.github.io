# Qwen2.5:3B

## Определение

**Qwen2.5:3B** — это компактная большая языковая модель (LLM) из семейства **Qwen2.5**, разработанного Alibaba Cloud (Qwen Team). Цифра **3B** означает около 3 миллиардов параметров. В экосистеме Ollama и на Hugging Face под тегом/именем `qwen2.5:3b` обычно доступна **instruction-tuned** (чат) версия модели, оптимизированная для диалогов, следования инструкциям и решения прикладных задач.

Архитектурно это decoder-only Transformer с улучшениями: RoPE (Rotary Position Embedding), SwiGLU, RMSNorm и grouped-query attention (GQA). Модель многоязычна (поддерживает английский, китайский, русский и многие другие языки), имеет словарь размером около 151 936 токенов и контекстное окно до **32 768 токенов** (32K) для версии 3B.

## Зачем нужно

- **Локальный запуск и приватность.** 3B параметров — это относительно небольшой размер, что позволяет запускать модель на потребительском железе (современные CPU, GPU с 6–8 ГБ VRAM в квантованном виде, например Q4_K_M) без обращения к облаку.
- **Баланс качества и ресурсов.** Qwen2.5:3B демонстрирует сильные для своего размера результаты в понимании языка, генерации кода, математике и рассуждениях, превосходя многие модели сопоставимого или даже большего размера предыдущих поколений.
- **Мультиязычность.** Хорошо подходит для русскоязычных и смешанных задач: ответы на вопросы, суммаризация, перевод, классификация, извлечение данных.
- **Гибкость интеграции.** Модель можно использовать через Ollama, llama.cpp, Hugging Face Transformers, vLLM и другие инструменты, встраивая в чат-ботов, RAG-системы, агентов и автоматизацию.
- **Экономичность.** Меньшие затраты на инференс по сравнению с 7B/14B/72B моделями при достаточном качестве для множества повседневных сценариев.

## Пример

Пример запуска через **Ollama** (предполагается, что Ollama уже установлена):

```bash
# Скачивание и запуск модели в интерактивном режиме
ollama run qwen2.5:3b

# Пример запроса в чате:
# >>> Напиши на Python функцию, которая возвращает факториал числа.
```

Пример использования через **Hugging Face Transformers** (Python):

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'Qwen/Qwen2.5-3B-Instruct'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype='auto',
    device_map='auto'
)

prompt = 'Объясни простыми словами, что такое RoPE в трансформерах.'
messages = [
    {'role': 'system', 'content': 'Ты полезный ассистент.'},
    {'role': 'user', 'content': prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = tokenizer(text, return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

Также можно использовать квантованные версии (GGUF) в **llama.cpp** или **LM Studio**, указав файл модели `qwen2.5-3b-instruct-q4_k_m.gguf` и контекст 32K.

## Проекты
- [ollama-agents](https://github.com/andand44/ollama-agents)
