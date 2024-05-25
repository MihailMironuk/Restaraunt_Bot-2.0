from aiogram import Router, F, types
from aiogram.filters import Command
from config import database
from pprint import pprint

food_router = Router()


@food_router.message(Command("menu"))
async def show_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Пицца"),
                types.KeyboardButton(text="Паста")
            ],
            [
                types.KeyboardButton(text="Салат"),

            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите из списка блюд", reply_markup=kb)


food_country = ("Америка", "Италия", "Норвегия")


@food_router.message(F.text.lower().in_(food_country))
async def show_country(message: types.Message):
    country = message.text
    print("Пользователь нажал на кнопку", country)
    data = await database.fetch(
        """SELECT * FROM food 
        INNER JOIN countries ON food.country_id = countries.id 
        WHERE countries.name = ?""",
        (country,)
    )
    pprint(data)
    if not data:
        await message.answer("Ничего не найдено")
        return
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Виды блюд {country}:", reply_markup=kb)
    for food in data:
        image = types.FSInputFile(food.get("picture"))
        await message.answer_photo(
            photo=image,
            caption=f"{food['name']} - {food['country']}\nЦена: {food['price']} сом")