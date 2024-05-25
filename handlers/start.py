from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_cmd(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://www.kfc.kg/"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/kfc.kg/?hl=ru")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
                types.InlineKeyboardButton(text="Парсер", callback_data="https://www.house.kg")
            ]
        ]
    )

    await message.answer(f"Привет, {message.from_user.first_name} я бот ресторана MegaRestik,"
                         f" здесь вы можете заказать себе покушать и просто хорошо провести время!"
                         f" Снизу навигация по нашим услугам.",  reply_markup=kb)


@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Наш ресторан, это место где встречаются вкус и стиль,"
                                  " чтобы создать незабываемый опыт для каждого гостя,"
                                  " мы гордимся нашим разнообразным меню, "
                                  " включающим в себя блюда для мясоедов,"
                                  " вегетарианцев, любителей морепродуктов и тех,"
                                  " кто следит за здоровым образом жизни.")