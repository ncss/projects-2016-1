import sqlite3
from models import User
from models import db

conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row


# Connect models
db.DatabaseObject.connect(conn)

if __name__ == "__main__":
	with open("sql/init.sql") as f:
		data = f.read()
	curr = conn.cursor()
	curr.executescript(data)

	