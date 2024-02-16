from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import settings
from sqlalchemy import text, MetaData
from sqlalchemy.orm import DeclarativeBase


async_engine = create_async_engine(
    url=settings.get_DB_URL,
    echo=True,
    )

async_session_factory = async_sessionmaker(bind=async_engine)

class Base(DeclarativeBase):
    pass

Base.metadata.create_all(async_engine)