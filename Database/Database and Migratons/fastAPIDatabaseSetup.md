## Setting up the Database in FastAPI 
1) Firstly setup the database you want to use.Eg
   
SQLALCHEMY_DATABASE_URL = "DBMS://username:password@host/database_name"
eg:"postgresql+psycopg2://postgres:9999@localhost/aron" 
2) Now you need to create engine :{The create_engine function is used to create an instance of a database engine.<br> It takes a connection URL (SQLALCHEMY_DATABASE_URL) as its first argument, which specifies the database <br>  connection string. This connection string contains information like the database <br> type (e.g., MySQL, PostgreSQL, SQLite), host, port, username, password, and database name. <br> The future=True argument enables SQLAlchemy's Future feature, which allows for asynchronous database operations.}{
This line creates an SQLAlchemy engine instance called engine. The create_engine function is used to create a new engine that connects to the database <br> specified in SQLALCHEMY_DATABASE_URL, which is the connection string for the database. The connect_args={} argument can be used to specify any <br>  extra arguments to be passed to the database driver during the connection, but in this case, <br> it's left empty. The future=True argument enables SQLAlchemy's Future feature, allowing asynchronous database operations.
}
3) Create a session local : SessionLocal is an instance of sessionmaker, which is a factory class for creating new SQLAlchemy <br> sessions. A session represents a transactional scope that communicates with the database. The autocommit and autoflush <br> parameters are set to False, which means the session will not automatically commit changes to the database or flush pending changes to <br> the database before executing a query. Setting bind=engine associates the session with the engine,<br>  so all operations performed within this session will use the specified database engine.
{
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True): This line creates an SQLAlchemy sessionmaker called SessionLocal. <br> The sessionmaker is a factory for creating new sessions. The autocommit=False means that the session<br>  will not automatically commit transactions, and autoflush=False means that it won't automatically flush pending changes to the database. <br> The bind=engine argument associates the session with the engine created earlier, so all operations performed within this session will<br>  use the specified database engine. The future=True argument enables asynchronous database operations for the session.
}
4) Create Base : Base is an instance of declarative_base, which is used to define the base <br> class for all the ORM model classes. It allows you to create Python classes that map to database tables.When defining<br>  ORM models, you should inherit from this base class.
5) Create DB Utility : This is a utility function called get_db. It's a generator function that provides a database session (db)<br>  to be used within a request or operation. The function uses the SessionLocal sessionmaker to create a new session (db) and then yields it to<br>  the calling function or route. After the yield statement, the session is automatically closed <br> using the finally block, ensuring proper cleanup of resources. This pattern is often used in web frameworks<br>  like FastAPI to manage database sessions during HTTP requests.
6)user_model.Base.metadata.create_all(bind=engine): This line invokes the create_all method on the metadata attribute of the Base<br>  class associated with the user_model. It creates the database table corresponding to the user_model class in <br> the database specified by the engine. Similarly, course_model.Base.metadata.create_all(bind=engine) creates the table for the course_model class.

async def get_user_course(user_id: int, db: Session = Depends(get_db)): ...: This is an asynchronous function called get_user_course, which takes two parameters: user_id of type int and db of type Session. The db parameter is a dependency injection that will automatically provide the database session (db) to this function. The Depends(get_db) means that this function depends on the get_db function, and FastAPI will call get_db to provide the database session to this route function.

Depends(get_db): This indicates that the db parameter will be populated by calling the get_db function using the Depends mechanism. The Depends mechanism is typically used in combination with a framework like FastAPI to handle dependency injection. It ensures that a new database session is created for each request and is properly closed after the request is processed.