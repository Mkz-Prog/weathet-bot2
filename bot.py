import os
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties  # <-- Добавь этот импорт
from dotenv import load_dotenv
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

# Загружаем переменные окружения
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Указываем параметры по умолчанию через DefaultBotProperties
bot = Bot(
    token=TELEGRAM_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # <-- Вот так!
)
dp = Dispatcher()

logging.basicConfig(filename="bot.log", level=logging.ERROR)





# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Введите команду /weather или /forecast")

# Обработчик /weather
@dp.message(Command("weather"))
async def cmd_weather(message: types.Message):
    try:
        # Получаем город из сообщения
        city = "Saint Petersburg"

        # Запрос к API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},ru&appid={WEATHER_API_KEY}&units=metric&lang=ru"
        data = requests.get(url).json()

        # Формируем ответ
        text = (
            f"🌤 Погода в городе {data['name']}:\n"
            f"🌡 Температура: {data['main']['temp']}°C\n"
            f"🌀 Ощущается как: {data['main']['feels_like']}°C\n"
            f"💨 Ветер: {data['wind']['speed']} м/с\n"
            f"🌫 Влажность: {data['main']['humidity']}%\n"
            f"📝 Описание: {data['weather'][0]['description'].capitalize()}"
        )

    except Exception as e:
        text = "⚠️ Ошибка при получении данных"
        print(f"Ошибка: {e}")

    await message.answer(text)


@dp.message(Command("forecast"))
async def cmd_forecast(message: types.Message):
    try:
        # Получаем город из сообщения
        city = "Saint Petersburg"

        # Запрос к API
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city},ru&appid={WEATHER_API_KEY}&units=metric&lang=ru"
        data = requests.get(url).json()

        # Формируем ответ
        text = f"🌤 Прогноз на 5 дней для города {data['city']['name']}:\n\n"
        for item in data['list'][::8]:  # Берем один прогноз в день (каждые 24 часа)
            date = item['dt_txt'].split()[0]
            temp = item['main']['temp']
            desc = item['weather'][0]['description'].capitalize()
            text += f"📅 {date}: {temp}°C, {desc}\n"

    except Exception as e:
        text = "⚠️ Ошибка при получении данных"
        print(f"Ошибка: {e}")

    await message.answer(text)

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/weather - Узнать погоду\n"
        "/forecast - Прогноз на 5 дней\n"
        "/help - Список команд"
    )
    await message.answer(text)



# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())