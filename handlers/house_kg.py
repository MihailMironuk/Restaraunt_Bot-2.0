import asyncio
from aiogram import types, Router
from aiogram.filters import Command
from httpx import AsyncClient
from parsel import Selector

parser_router = Router()


async def get_page(url: str, client: AsyncClient):
    response = await client.get(url)
    print("Status:", response.status_code, "url:", url)
    return response.text


class HouseKgCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    def get_links(self, html):
        selector = Selector(text=html)
        links = selector.css("div.list-item a::attr(href)").getall()
        links = [self.BASE_URL + x for x in links]
        return links

    async def get_links_from_all_pages(self):
        async with AsyncClient() as client:
            tasks = []
            for i in range(1, 11):
                url = f"{self.MAIN_URL}?page={i}"
                task = asyncio.create_task(get_page(url, client))
                tasks.append(task)

            pages = await asyncio.gather(*tasks)
            all_links = []
            for page in pages:
                links = self.get_links(page)
                all_links.extend(links)

            return all_links[:3]


async def start_crawler(message: types.Message):
    await message.answer("Запуск парсера...")
    crawler = HouseKgCrawler()
    links = await crawler.get_links_from_all_pages()
    for link in links:
        await message.answer(link)


@parser_router.message(Command("/parser"))
async def show_crawler(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton("Парсер")]
        ],
        resize_keyboard=True
    )
    await message.answer(text="Нажмите кнопку для запуска парсера", reply_markup=kb)


if __name__ == "__main__":
    crawler = HouseKgCrawler()
    asyncio.run(crawler.get_links_from_all_pages())