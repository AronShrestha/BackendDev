import databases
import sqlalchemy
from datetime import datetime


DATABASE_URL="sqlite:///test.db"


# Create the database engine
engine = sqlalchemy.create_engine(DATABASE_URL)

# Database table definitions.
metadata = sqlalchemy.MetaData()

#Defining the model 
todo = sqlalchemy.Table(
    "todo",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable =True),
    sqlalchemy.Column("description",sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now)
)

database = databases.Database(DATABASE_URL)


