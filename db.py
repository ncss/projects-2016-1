import sqlite3
from models import User

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row

# Connect models
User.connect(conn)
