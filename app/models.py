from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class WorkerOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]

