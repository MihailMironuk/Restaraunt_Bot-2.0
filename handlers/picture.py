from aiogram import Router, types
from aiogram.filters import Command
import random

picture_router = Router()


@picture_router.message(Command("picture"))
async def random_pic(message: types.Message):
    photo = (
        "pic1.jpg",
        "pic2.jpg",
        "pic3.jpg",
        "pic4.jpg",
        "pic5.jpg"
    )
    random_image = random.choice(photo)
    photo_directory = f"images/{random_image}"
    photo = types.FSInputFile(photo_directory)
    await message.reply_photo(photo)