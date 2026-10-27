# Telegram

# Telegram

## Определение

**Telegram** — это кроссплатформенный облачный мессенджер и платформа для общения, запущенная Павлом Дуровым в 2013 году. Сервис использует проприетарный протокол **MTProto** и предоставляет обмен текстовыми сообщениями, голосовыми и видеозвонками, файлами, а также инструменты для создания групп, каналов, ботов и мини-приложений. Telegram доступен на iOS, Android, Windows, macOS, Linux и в веб-версии, а данные синхронизируются между устройствами через облако.

## Зачем нужно

Telegram применяется как для личного общения, так и для бизнес- и разработческих задач:

- **Быстрый и защищённый обмен сообщениями** — облачная синхронизация, секретные чаты с end-to-end шифрованием, голосовые и видеозвонки.
- **Сообщества и каналы** — группы до сотен тысяч участников и каналы для вещания контента на неограниченную аудиторию.
- **Автоматизация через ботов** — Telegram Bot API позволяет создавать чат-ботов для поддержки, уведомлений, платежей и интеграций с внешними сервисами.
- **Разработка мини-приложений** — встроенные веб-приложения (Telegram Web Apps) и Telegram Login для авторизации на сторонних сайтах.
- **Обмен файлами** — передача документов, медиа и архивов размером до 2 ГБ.
- **Интеграции и уведомления** — отправка сообщений из CI/CD, мониторинга, CRM и других систем через Bot API.

## Пример

Ниже приведён минимальный пример эхо-бота на Python с использованием библиотеки `python-telegram-bot` (v20+). Бот отвечает на команду `/start` и повторяет текстовые сообщения пользователя.

```python
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я эхо-бот. Напиши мне что-нибудь.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == "__main__":
    main()
```

Отправить сообщение можно и напрямую через HTTP-запрос к Bot API:

```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" -d "chat_id=<CHAT_ID>" -d "text=Привет из Telegram Bot API!"
```

## Проекты
- [ollama-agents](https://github.com/andand44/ollama-agents)
