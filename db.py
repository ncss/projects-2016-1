import sqlite3
from models import User
from models import db

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row

# Connect models
db.DatabaseObject.connect(conn)
