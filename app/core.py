from pydantic import EmailStr
from sqlalchemy import Table, MetaData, String, Integer, ForeignKey, Column, Text, insert
from database import sync_engine

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

user_data = [
    {'name':'John', 'email': 'a@a.com'},
    {'name':'Alex', 'email': 'c@a.com'},
    {'name':'Sam', 'email': 'cd@a.com'}
]

users_bio = [
    {'id':1, 'user_id':2, 'bio': 'i`m a frontend developer'},
    {'id':2, 'user_id':3, 'bio': 'i`m a backend developer'},
    {'id':3, 'user_id':1, 'bio': 'i`m a fullstack developer'}

]
roles_data = [
    {'name': 'ADMIN'},
    {'name': 'USER'}
]

user_roles_data = [
    {'user_id': 1, 'role_id':1},
    {'user_id': 2, 'role_id':1},
    {'user_id': 3, 'role_id':2},
]

with sync_engine.connect() as conn:
    conn.execute(insert(users), user_data)
    conn.execute(insert(users_profiles), users_bio)
    conn.execute(insert(roles), roles_data)
    conn.execute(insert(user_roles), user_roles_data)
    conn.commit()