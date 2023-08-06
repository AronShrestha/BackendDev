#### Explored on SQLALCHEMY , async SQLALCHEMY and how to use raw Query on async SQL alchemy

#### config for async SQLALCHEMY
```
ASYNC_SQLALACHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_username}:{db_password}@localhost/{database}"  
# notice it uses asyncpg :asyncpg is an asynchronous PostgreSQL database #   client for Python. It provides support for asynchronous interactions #   with PostgreSQL databases, which is particularly useful in asynchronous # web applications and frameworks like Starlette, FastAPI, and others.


# creating engine for async 
from sqlalchemy.sql import text

async_engine = create_async_engine(ASYNC_SQLALACHEMY_DATABASE_URL)

# working with async engine using raw query
  email = data['email']
    async with async_engine.connect() as connection:
        query = text("select email, password from users where email = :email")
        result = await connection.execute(query.bindparams(email=email))
        user = result.fetchone()
        print({"email":user.email})

```
 
 #### Finding on Postgres :String field can't store hashed password in byte code form and stores as different string that cannot be used to validate the password as when saved it's form is changed and when we check_password it doesn't match with the hash of password given by user via post request.

#### Solution:
#### Use field LargeBinary for storing the hashed password.