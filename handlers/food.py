from aiogram import Router, F, types
from aiogram.filters import Command
from config import database
from pprint import pprint

restaurant_router = Router()


@restaurant_router.message(Command("menu"))
async def show_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="бургеры"),
                types.KeyboardButton(text="мясо по-итальянски")
            ],
            [
                types.KeyboardButton(text="шашлычки"),

            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите категорию блюда кнопой справа", reply_markup=kb)


dish_categories = ("бургеры", "мясо по-итальянски", "шашлычки")


@restaurant_router.message(F.text.lower().in_(dish_categories))
async def show_dish_by_category(message: types.Message):
    category = message.text
    print("Пользователь нажал на кнопку", category)
    data = await database.fetch(
        """SELECT * FROM dishes 
        INNER JOIN categories ON dishes.category = categories.id 
        WHERE categories.name = ?""",
        (category,)
    )
    pprint(data)
    if not data:
        await message.answer("В наличии таких блюд пока нет, приносим извинения")
        return
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Все блюда {category}:", reply_markup=kb)
    for dish in data:
        # image = types.FSInputFile(dish.get("picture"))
        await message.answer(text=f"{dish['name']}\nСтрана производитель - {dish['country']}\nЦена: {dish['price']} сом")