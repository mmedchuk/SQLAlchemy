from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import settings
from sqlalchemy import text
import asyncio


async_engine = create_async_engine(
    url=settings.get_DB_URL,
    echo=True,
    )

async def get_async_connect():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        return res


asyncio.run(get_async_connect())