"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from models import Base, Session, User, Post, engine
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_users_to_db(users_data):
    async with Session() as session:
        users = [
            User(id=user["id"], name=user["name"], username=user["username"], email=user["email"])
            for user in users_data
        ]
        session.add_all(users)
        await session.commit()
        return users


async def add_posts_to_db(posts_data):
    async with Session() as session:
        posts = [
            Post(id=post["id"], user_id=post["userId"], title=post["title"], body=post["body"])
            for post in posts_data
        ]
        session.add_all(posts)
        await session.commit()
        return posts


async def async_main():
    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    await asyncio.gather(
        add_users_to_db(users_data),
        add_posts_to_db(posts_data)
    )

    print("✅ Данные успешно загружены в базу данных.")


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()