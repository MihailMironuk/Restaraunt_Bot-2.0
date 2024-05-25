import aiosqlite
from database.queries import Queries


class Database:
    def __init__(self, path: str) -> None:
        self.path = path

    async def create_tables(self) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute(Queries.CREATE_SURVEY_TABLE)
            await db.execute(Queries.DROP_COUNTRIES_TABLE)
            await db.execute(Queries.CREATE_COUNTRIES_TABLE)
            await db.execute(Queries.DROP_FOOD_TABLE)
            await db.execute(Queries.CREATE_FOOD_TABLE)
            await db.execute(Queries.POPULATE_COUNTRIES)
            await db.execute(Queries.POPULATE_FOOD)
            await db.commit()

    async def execute(self, query: str, params: tuple | None = None) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute(query, params or ())
            await db.commit()

    async def fetch(self, query: str, params: tuple | None = None, fetch_type: str = "all"):
        async with aiosqlite.connect(self.path) as db:
            db.row_factory = aiosqlite.Row
            data = await db.execute(query, params or ())

            if fetch_type == 'all':
                result = await data.fetchall()
                return [dict(row) for row in result]

            if fetch_type == 'one':
                result = await data.fetchone()
                return dict(result)