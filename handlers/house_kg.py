from aiogram import types, Dispatcher
from parser.crawler import HouseKgCrawler


async def start_crawler(message: types.Message):
    await message.answer("Запуск парсера...")
    crawler = HouseKgCrawler()
    links = await crawler.get_links_from_all_pages()
    for link in links[:3]:
        await message.answer(link)


def setup_commands(dp: Dispatcher):
    @dp.message_handler(commands=["parser"])
    async def show_crawler(message: types.Message):
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton("Парсер")]
            ],
            resize_keyboard=True
        )
        await message.answer(text="Нажмите кнопку для запуска парсера", reply_markup=kb)

    @dp.message_handler(lambda message: message.text == "Парсер")
    async def handle_crawler_button(message: types.Message):
        await start_crawler(message)
