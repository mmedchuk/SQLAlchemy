from sqlalchemy import text, insert
from database import sync_engine, sync_session_factory, Base
from models import WorkerOrm



def create_table():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


create_table()


def insert_data():
    with sync_session_factory() as conn:
        worker_1 = WorkerOrm(name='Olha')
        worker_2 = WorkerOrm(name='sv')
        conn.add(worker_1)
        conn.add(worker_2)
        conn.commit()
        

# def insert_data_ns():
#     with sync_engine.connect() as conn:
#         stmt = insert(workers_table).values([
#             {"username": "olha"},
#             {"username": "sv"}
#         ])
#         conn.execute(stmt)

#         conn.commit()

insert_data()