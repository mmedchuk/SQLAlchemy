from datetime import datetime
from enum import Enum
from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import ForeignKey, Table, Column, String, MetaData, Integer, text


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow())]


class WorkerOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    name:Mapped[str]


class Workload(Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumeOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    title : Mapped[str]
    salary: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]








# metadata_obj= MetaData()


# workers_table = Table(
#     'workers',
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('username', String)
# )



