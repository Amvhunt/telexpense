import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()  # Эта строка загрузит переменные из .env

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN = os.getenv("ADMINS", "").split(",")
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")

# Дальше ваш код без изменений
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
    # Импорт и регистрация хендлеров
    register_all_handlers(dp)
    executor.start_polling(dp, skip_updates=True)

# Configure logging
logging.basicConfig(level=logging.INFO)

#def register_all_handlers(dp):
    # Registering commands #available for unregistered users
   # register_start_help(dp)

    # Registering commands for registration
    #register_registration(dp)

    # Registering comands for all users
    register_maincurrency(dp)
    #register_user(dp)
    register_expenses(dp)
    register_income(dp)
    register_transfer(dp)


# Initialize bot and dispatcher
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":
    from handlers.expenses import register_expenses
    from handlers.income import register_income
    from handlers.maincurrency import register_maincurrency
   # from handlers.registration import register_registration
    from handlers.transfer import register_transfer
    #from handlers.user import register_start_help, register_user


    register_all_handlers(dp)

    executor.start_polling(dp, skip_updates=True)
