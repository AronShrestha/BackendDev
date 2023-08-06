from database.database_config import async_engine
from sqlalchemy.sql import text


async def get_users():
    async with async_engine.connect() as connection:
        query = text("select * from users")
        response = await connection.execute(query)
        response_data = response.fetchall()
        return response_data


