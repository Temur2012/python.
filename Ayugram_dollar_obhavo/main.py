import os
import asyncio
import requests
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


logging.basicConfig(level=logging.INFO)

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌤 Ob-havo"),
            KeyboardButton(text="💵 Dollar kursi")
        ]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start_command(message: types.Message):
    text = f"Salom {message.from_user.first_name}! Nima haqida ma'lumot olmoqchisiz?"
    await message.answer(text, reply_markup=menu)


@dp.message(F.text == "💵 Dollar kursi")
async def get_currency(message: types.Message):
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    try:
        response = requests.get(url)
        data = response.json()
        usd = next(item for item in data if item['Ccy'] == 'USD')
        await message.answer(f"🇺🇸 1 Dollar = {usd['Rate']} so'm\n📅 Sana: {usd['Date']}")
    except:
        await message.answer("Kurs ma'lumotlarini olishda xatolik yuz berdi.")



@dp.message(F.text == "🌤 Ob-havo")
async def get_weather(message: types.Message):
    city = "Urgench"
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            temp = current['temp_C']
            desc = current['lang_uz'][0]['value'] if 'lang_uz' in current else \
            current['weatherDesc'][0]['value']

            await message.answer(
                f"📍 {city} shahri\n"
                f"🌡 Harorat: {temp}°C\n"
                f"☁️ Holat: {desc}"
            )
        else:
            await message.answer("Ob-havo ma'lumotlarini olishda muammo yuz berdi.")
    except Exception as e:
        logging.error(f"Xatolik: {e}")
        await message.answer("Server bilan bog'lanishda xatolik.")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")