from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import database

survey_router = Router()


class FoodSurvey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    food = State()
    country = State()
    rating = State()


@survey_router.message(Command("review"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(FoodSurvey.name)
    await message.answer("Как вас зовут?")


@survey_router.message(FoodSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await state.set_state(FoodSurvey.age)
    await message.answer("Сколько вам лет?")


@survey_router.message(FoodSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    age = int(age)
    if age < 18 or age > 54:
        await message.answer("Пожалуйста, введите возраст от 18 до 54")
        return
    await state.update_data(age=age)
    await state.set_state(FoodSurvey.gender)
    await message.answer("Ваш пол?")


@survey_router.message(FoodSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    await state.set_state(FoodSurvey.food)
    await message.answer("Ваше любимое блюдо?")


@survey_router.message(FoodSurvey.food)
async def process_food(message: types.Message, state: FSMContext):
    food = message.text
    await state.update_data(food=food)
    await state.set_state(FoodSurvey.country)
    await message.answer("Любимое иностранное блюдо?")


@survey_router.message(FoodSurvey.country)
async def process_country(message: types.Message, state: FSMContext):
    country = message.text
    await state.update_data(country=country)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="отлично")],
            [types.KeyboardButton(text="хорошо")],
            [types.KeyboardButton(text="плохо")]
        ],
        resize_keyboard=True
    )
    await state.set_state(FoodSurvey.rating)
    await message.answer("Поставьте нам рейтинг:", reply_markup=kb)


ratings = ["плохо", "хорошо", "отлично"]


@survey_router.message(FoodSurvey.rating, F.text.lower().in_(ratings))
async def process_rating(message: types.Message, state: FSMContext):
    rating = message.text
    rating = ratings.index(rating) + 3
    await state.update_data(rating=rating)
    await message.answer(f"Спасибо за прохождение опроса, {message.from_user.full_name}!")
    data = await state.get_data()
    print(data)
    await database.execute(
        "INSERT INTO surveys (name, age, gender, food, country, rating) VALUES (?, ?, ?, ?, ?)",
        (data["name"], data["age"], data["gender"], data["food"], data["country"], data["rating"]),
    )
    await state.clear()