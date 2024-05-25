from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from database.database import Database
from pathlib import Path

database = Database(Path('__file__').parent / 'db.sqlite')

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


async def set_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="picture", description="Картинка"),
        types.BotCommand(command="review", description="Пройдите опрос"),
        types.BotCommand(command="menu", description="Наше меню"),
        types.BotCommand(command="parser", description="Парсер")
    ])