from aiogram import Router, types

echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    await message.answer("""Я не понимаю Вас. Вот команды, которые я знаю:
    /start - начало
    /picture - картинка
    /review - опрос
    /menu - меню
    /parser - парсер""")