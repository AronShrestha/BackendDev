 Starlet walkthrough

## Trying database connection and simple curd Application in Starlet

### Database connection :
1) Firstly, get the choice of your database, and configue its url eg: DATABASE_URL="sqlite:///test.db"

2) Give database table definition :The sqlalchemy.MetaData() function is called to create an instance of the MetaData class. This instance, named metadata in this case, acts as a container that holds information about the database schema and all its components.[metadata = sqlalchemy.MetaData()]

3) Then we need to create the database connection:we need to create object of  'Database' class from module 'database', which will take 'DATABASE_URL' as an argument.[database = databases.Database(DATABASE_URL)]
4) Now you need to define the async context manager to fulfill the necessay database connectivity and disconectivity operations.The await keyword is used to asynchronously connect to the database using the database object. the lifespan async context manager is used to manage the database connection for an asynchronous web application. It establishes the database connection before the application starts running, yields control to the application for its execution, and then disconnects from the database after the application is done. This approach ensures proper handling of the database connection during the lifespan of the application and helps maintain good resource management practices in an asynchronous environment.
[
@contextlib.asynccontextmanager
async def lifespan(app):
    await database.connect()
    yield
    await database.disconnect()
]
5) Now we can start making model and necessary logic for endpoint we want to hit 