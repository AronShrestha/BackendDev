
we need flask_migrate to make migration using Migrate ("i.e : from flask_migrate import Migrate")
then we need to setup "FLASK_APP" in environment variable : in Linux we can do that by 
"FLASK_APP={nameofmainfile}"->FLASK_APP=main.py

Then we need to create the migration reprository with the command :"flask db init"
this will add a migration folder to our application. The contents of this folder need to be added to version control along with our other source files.

Then we can generate initial migration by :
flask db migrate -m "description of migration"
After which we can apply the changes described by the migration script to our database
flask db upgrade

