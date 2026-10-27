# aiogram

### Определение
**aiogram** — это современный, полностью асинхронный фреймворк для разработки Telegram-ботов на языке Python. Он построен на базе стандартной библиотеки `asyncio` и `aiohttp`, что позволяет эффективно работать с Telegram Bot API без блокировки основного потока выполнения.

### Зачем нужно
aiogram используется для создания масштабируемых и производительных Telegram-ботов. Основные преимущества:
- **Асинхронность:** Позволяет обрабатывать тысячи одновременных запросов, не замедляя работу бота.
- **FSM (Конечные автоматы):** Встроенная поддержка конечных автоматов упрощает создание сложных многошаговых сценариев общения с пользователем (например, форм регистрации или заказов).
- **Удобство и лаконичность:** Понятный синтаксис с использованием декораторов и фильтров делает код чистым и легко читаемым.
- **Актуальность:** Оперативная поддержка новых функций Telegram Bot API.

### Пример
Простейший пример эхо-бота, который отвечает на команду `/start` и повторяет отправленные сообщения:

```python
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Токен вашего бота
API_TOKEN = 'YOUR_BOT_TOKEN'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я эхо-бот. Напиши мне что-нибудь.")

# Обработчик всех остальных текстовых сообщений
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

# Функция запуска бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
```

## Проекты
- [ollama-agents](https://github.com/andand44/ollama-agents)
