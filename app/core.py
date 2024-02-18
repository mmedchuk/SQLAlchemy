from sqlalchemy import text, insert
from database import sync_engine, sync_session_factory, Base
from models import WorkerOrm, ResumeOrm



def create_table():
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


create_table()


def insert_data():
    with sync_session_factory() as conn:
        worker_1 = WorkerOrm(name='Olha')
        worker_2 = WorkerOrm(name='sv')
        resume_1 = ResumeOrm(title='Senior Python', salary=1000, workload='parttime', worker_id=2)
        resume_2 = ResumeOrm(title='Junior Python', salary=3000, workload='fulltime', worker_id=1)
        conn.add_all([worker_1, worker_2])
        conn.commit()
        conn.add_all([resume_1, resume_2])
        conn.commit()
        
insert_data()






# def insert_data_ns():
#     with sync_engine.connect() as conn:
#         stmt = insert(workers_table).values([
#             {"username": "olha"},
#             {"username": "sv"}
#         ])
#         conn.execute(stmt)

#         conn.commit()
