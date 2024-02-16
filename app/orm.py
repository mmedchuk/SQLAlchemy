import models
from database import async_session_factory, Base, async_engine
import asyncio


def create_table():
    Base.metadata.create_all()

async def insert_data():
    async with async_session_factory() as session:
        session.add(models.WorkerOrm(name='Ivan'))
        await session.commit()

create_table()
asyncio.run(insert_data())
