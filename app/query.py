from sqlalchemy import select
from database import sync_engine
from core import users, users_profiles,user_roles, roles


with sync_engine.connect() as conn:
    # query = (
    # select(users.c.id, users.c.name, users_profiles.c.bio)
    # .select_from(users.join(users_profiles, users.c.id == users_profiles.c.user_id)))
    query = (
        select(users.c.id, users.c.name, roles.c.name)
        .select_from(users)
        .join(user_roles, users.c.id==user_roles.c.user_id)
        .join(roles, user_roles.c.role_id==roles.c.id)
        # .join(users_profiles, users.c.id==users_profiles.c.user_id)
        )
    result = conn.execute(query)
    for statement in result:
        # print(f'I`m {statement.name}. My id is {statement.id}. Profession: {statement.bio}')
        print(statement)