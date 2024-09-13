from config import settings
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData, Integer, String, ForeignKey, insert, select, or_

engine = create_engine(settings.get_sync_DB_URL, echo=True)

metadata = MetaData()

worker = Table(
    'workers',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, unique=True)
)

salary = Table(
    'salaries',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('worker', Integer, ForeignKey(worker.c.id, ondelete='CASCADE', onupdate='CASCADE')),
    Column('total', Integer)
)

def manage_db(method:str):
    method(engine)

def insert_data():
    workers = [
        {'id':1, 'name': 'John'},
        {'id':2, 'name': 'Jack'}
        ]
    
    salaries = [
        {'id':1, 'worker':1, 'total':1000},
        {'id':2, 'worker':2, 'total':15800}
    ]

    with engine.begin() as connection:
        connection.execute(insert(worker).values(workers))
        connection.execute(insert(salary).values(salaries))
        connection.commit()

def select_data():
    query = select(worker.c.name, salary.c.worker, salary.c.total).select_from(worker.join(salary, worker.c.id == salary.c.worker)).where(or_(salary.c.total>1000),(worker.c.name.contains('Jack')))
    result = engine.connect().execute(query)
    print(result.all())

# manage_db(metadata.create_all)
# insert_data()
select_data()
