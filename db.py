import sqlite3
from models import List, User

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row


# Connect models to SQLite3 Instance
List.connect(conn)
User.connect(conn)
