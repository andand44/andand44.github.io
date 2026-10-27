# Server-Sent Events

# Server-Sent Events (SSE)

## Определение
**Server-Sent Events (SSE)** — это технология, позволяющая веб-серверу автоматически отправлять обновления клиенту (например, браузеру) через стандартное HTTP-соединение. Она основана на использовании MIME-типа `text/event-stream` и обеспечивает одностороннюю связь: только от сервера к клиенту. В отличие от WebSockets, SSE работает поверх обычного HTTP, что упрощает её интеграцию и использование.

## Зачем нужно
Технология SSE применяется там, где клиенту требуется получать данные в реальном времени без необходимости постоянной отправки запросов на сервер (поллинга). Основные сценарии использования:
- **Уведомления и ленты активности:** мгновенная доставка новых сообщений или уведомлений.
- **Стриминг данных:** обновление курсов валют, котировок акций или спортивных счетов в реальном времени.
- **Отображение прогресса:** отслеживание статуса длительных операций на сервере (например, генерация отчетов).
- **Ответы LLM:** потоковая передача ответов от больших языковых моделей (как в ChatGPT), чтобы текст появлялся по мере генерации.

## Пример

### Клиентская часть (JavaScript)
Создание подключения и прослушивание событий с помощью встроенного API `EventSource`:

```javascript
// Создаем объект EventSource, указывая URL эндпоинта на сервере
const eventSource = new EventSource('/api/updates');

// Обработчик получения сообщений
eventSource.onmessage = function(event) {
    console.log('Получены данные:', event.data);
};

// Обработчик ошибок
eventSource.onerror = function(error) {
    console.error('Произошла ошибка:', error);
};
```

### Серверная часть (Node.js + Express)
Настройка эндпоинта, который будет отправлять данные клиенту:

```javascript
const express = require('express');
const app = express();

app.get('/api/updates', (req, res) => {
    // Устанавливаем необходимые заголовки для SSE
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');
    res.flushHeaders(); // Отправляем заголовки сразу

    let counter = 0;
    
    // Отправляем сообщение клиенту каждую секунду
    const intervalId = setInterval(() => {
        counter++;
        // Формат сообщения: "data: <полезная нагрузка>\n\n"
        res.write(`data: Текущее время: ${new Date().toLocaleTimeString()} (сообщение №${counter})\n\n`);
    }, 1000);

    // Очистка ресурсов при отключении клиента
    req.on('close', () => {
        clearInterval(intervalId);
        res.end();
    });
});

app.listen(3000, () => {
    console.log('Сервер запущен на http://localhost:3000');
});
```

## Проекты
- [enterprise-rag-service](https://github.com/andand44/enterprise-rag-service)
