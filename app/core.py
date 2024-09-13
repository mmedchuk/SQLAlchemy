from pydantic import EmailStr
from sqlalchemy import Table, MetaData, String, Integer, ForeignKey, Column, Text, insert
from database import sync_engine
from input_data import *

metadata = MetaData()


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String), 
    Column('email', String, unique=True)

)

users_profiles = Table(
    'users_profiles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey(users.c.id, ondelete="CASCADE"), nullable=False),
    Column('bio', Text)
)

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String())
)

user_roles = Table(
    'user_roles',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('role_id', Integer, primary_key=True)
)

metadata.drop_all(sync_engine)
metadata.create_all(sync_engine)

with sync_engine.connect() as conn:
    conn.execute(insert(users), user_data)
    conn.execute(insert(users_profiles), users_bio)
    conn.execute(insert(roles), roles_data)
    conn.execute(insert(user_roles), user_roles_data)
    conn.commit()