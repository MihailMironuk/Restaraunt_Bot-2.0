from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from database.database import Database
from pathlib import Path

load_dotenv()
database = Database(Path('__file__').parent / 'db.sqlite')

dev = getenv("DEV", 0)
if not dev:
    from aiogram.client.session.aiohttp import AiohttpSession

    print("Started on serve")
    session = AiohttpSession(proxy=getenv("PROXY"))
    bot = Bot(token=getenv("BOT_TOKEN"), session=session)
else:
    print("Started on dev")
    bot = Bot(token=getenv("BOT_TOKEN"))

dp = Dispatcher()


async def set_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="picture", description="Картинка"),
        types.BotCommand(command="review", description="Пройдите опрос"),
        types.BotCommand(command="menu", description="Наше меню")
    ])
