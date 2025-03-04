# weathet-bot2

# Погодный бот для Санкт-Петербурга в Telegram

Бот предоставляет актуальную информацию о погоде и прогнозе в Санкт-Петербурге.

## Установка

1. Клонируйте репозиторий
2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Настройка

1. Получите API-токены:
   - Telegram Bot Token через [@BotFather](https://t.me/BotFather)
   - OpenWeatherMap API ключ на [openweathermap.org](https://openweathermap.org/api)

2. Создайте файл `.env` в корне проекта:
```ini
TELEGRAM_TOKEN=ваш_телеграм_токен
WEATHER_API_KEY=ваш_owm_ключ
```

## Команды бота

- `/start` - Начало работы
- `/weather` - Текущая погода
- `/forecast` - Прогноз на 5 дней
- `/help` - Справка по командам

## Запуск

```bash
python bot.py
```

## Пример ответа

При выполнении `/weather`:
```
🌤 Погода в городе Saint Petersburg:
🌡 Температура: 18°C
🌀 Ощущается как: 16°C
💨 Ветер: 3 м/с
🌫 Влажность: 65%
📝 Описание: Облачно с прояснениями
```

## Зависимости

- Python 3.9+
- aiogram >= 3.0
- python-dotenv >= 0.19
- requests >= 2.26
