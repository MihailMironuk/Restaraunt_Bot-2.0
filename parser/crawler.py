import asyncio
from httpx import AsyncClient
from parsel import Selector


class HouseKgCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    def get_links(self, html):
        selector = Selector(text=html)
        links = selector.css("a.item-title::attr(href)").getall()
        links = [self.BASE_URL + x for x in links]
        return links

    async def get_links_from_all_pages(self):
        async with AsyncClient() as client:
            tasks = []
            for i in range(1, 11):
                url = f"{self.MAIN_URL}?page={i}"
                task = asyncio.create_task(self.get_page(url, client))
                tasks.append(task)

            pages = await asyncio.gather(*tasks)
            all_links = []
            for page in pages:
                links = self.get_links(page)
                all_links.extend(links)

            return all_links

    async def get_page(self, url: str, client: AsyncClient):
        response = await client.get(url)
        print("Status:", response.status_code, "url:", url)
        return response.text