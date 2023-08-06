from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DATABASE')
print("Password is :", db_password)
SQLALACHEMY_DATABASE_URL = f"postgresql+psycopg2://{db_username}:{db_password}@localhost/{database}"
ASYNC_SQLALACHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_username}:{db_password}@localhost/{database}"              


engine = create_engine(
                        SQLALACHEMY_DATABASE_URL,
                        connect_args={},
                        future=True
)

#creating engine for async 
async_engine = create_async_engine(ASYNC_SQLALACHEMY_DATABASE_URL)

session_local = sessionmaker(
                            autocommit=False,
                            autoflush=False,
                            bind=engine,
                            future=True
)

Base = declarative_base()


# db = session_local() #here db is the database session 

# better approach for using session manager with context manager


from contextlib import  contextmanager


@contextmanager
def session_local_manager():
    session = session_local() # creating the session instance
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()