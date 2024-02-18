from models import WorkerOrm
from database import sync_session_factory



with sync_session_factory() as session:
    session.add(WorkerOrm.name=='Ivan')
    session.commt()
