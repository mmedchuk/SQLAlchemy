from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import Table, Column, String, MetaData, Integer


metadata_obj= MetaData()


workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)







class WorkerOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]

