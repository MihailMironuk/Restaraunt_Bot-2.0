import asyncio
import logging
from aiogram import Bot

from config import bot, dp, set_menu, database
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.food import food_router
from handlers.survey import survey_router
from handlers.picture import picture_router
from handlers.house_kg import parser_router


async def on_startup(bot: Bot) -> None:
    await database.create_tables()


async def main():
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(survey_router)
    dp.include_router(food_router)
    dp.include_router(parser_router)

    dp.include_router(echo_router)

    await set_menu()
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())