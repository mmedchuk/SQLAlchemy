from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import settings
from sqlalchemy import text, MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import asyncio

sync_engine = create_engine(
    url=settings.get_sync_DB_URL,
    echo=True
)

async_engine = create_async_engine(
    url=settings.get_async_DB_URL,
    echo=True,
    )

sync_session_factory = sessionmaker(bind=sync_engine)
async_session_factory = async_sessionmaker(bind=async_engine)

class Base(DeclarativeBase):
    pass
