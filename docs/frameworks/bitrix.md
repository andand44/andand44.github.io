# Bitrix

# Bitrix

## Определение
**Bitrix** (чаще **1С-Битрикс** или **Битрикс24**) — коммерческая CMF/CMS-платформа (Content Management Framework) для разработки и управления веб-проектами: сайтами, интернет-магазинами, корпоративными порталами и личными кабинетами. Ядро написано на **PHP**, для хранения данных используются **MySQL/MariaDB** и другие СУБД. Платформа включает собственный фреймворк (Bitrix Framework), ORM D7, готовые модули, компоненты и шаблоны. Облачная экосистема **Битрикс24** дополняет её CRM, задачами и инструментами совместной работы.

## Зачем нужно
- **Быстрый запуск проектов**: готовые модули (каталог, корзина, заказы, оплата, доставка) и визуальные компоненты позволяют собрать сайт без написания всей логики с нуля.
- **Интеграции**: встроенная синхронизация с **1С**, платёжными системами, службами доставки, маркетплейсами и внешними API.
- **Гибкость для разработчиков**: собственный API, ORM D7, обработчики событий, агенты, кеширование, шаблоны сайтов и компонентов.
- **Безопасность и поддержка**: регулярные обновления, встроенные механизмы защиты (проактивная защита, фильтрация), техническая поддержка вендора.
- **Единая экосистема**: связь сайта с CRM, сквозной аналитикой и бизнес-процессами через Битрикс24.

## Пример
### Использование стандартного компонента
Пример вывода списка новостей из инфоблока с помощью компонента `bitrix:news.list`:

```php
<?php
// Подключение компонента в шаблоне сайта
$APPLICATION->IncludeComponent(
    'bitrix:news.list',
    '.default',
    [
        'IBLOCK_ID'     => 5,               // ID инфоблока «Новости»
        'NEWS_COUNT'    => 10,              // Количество новостей
        'SORT_BY1'      => 'ACTIVE_FROM',
        'SORT_ORDER1'   => 'DESC',
        'FIELD_CODE'    => ['NAME', 'PREVIEW_TEXT', 'DETAIL_PAGE_URL'],
        'PROPERTY_CODE' => [''],
        'SET_TITLE'     => 'N',
        'CACHE_TIME'    => 3600,
    ]
);
?>
```

### Работа с API (ORM D7)
Пример получения активных элементов инфоблока через ORM D7:

```php
<?php
require($_SERVER['DOCUMENT_ROOT'] . '/bitrix/modules/main/include/prolog_before.php');

use Bitrix\Main\Loader;
use Bitrix\Iblock\ElementTable;

if (Loader::includeModule('iblock')) {
    $result = ElementTable::getList([
        'select' => ['ID', 'NAME', 'PREVIEW_TEXT'],
        'filter' => ['=IBLOCK_ID' => 5, '=ACTIVE' => 'Y'],
        'order'  => ['SORT' => 'ASC'],
        'limit'  => 10,
    ]);

    while ($element = $result->fetch()) {
        echo '<h2>' . htmlspecialchars($element['NAME']) . '</h2>';
        echo '<p>' . htmlspecialchars($element['PREVIEW_TEXT']) . '</p>';
    }
}

require($_SERVER['DOCUMENT_ROOT'] . '/bitrix/modules/main/include/epilog_after.php');
?>
```

## Проекты
- [albina](https://github.com/andand44/albina)
