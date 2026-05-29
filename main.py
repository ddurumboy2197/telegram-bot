import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'VINGIZNI KIRITING'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Men sizga xush kelibsiz.")

@dp.message_handler()
async def echo_message(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. `API_TOKEN` ni o'zingizning Telegram bot API tokeni bilan almashtiring.
2. Kodni `main.py` deb nomlangan yangi faylga saqlang.
3. `pip install aiogram` komandasi orqali `aiogram` kutubxonasini o'rnatib oling.
4. `python main.py` komandasi orqali botni ishga tushiring.
