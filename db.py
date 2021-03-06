import sqlite3
import os

from models import User
from models import List
from models import ListContent

from models import db

DATABASE_FILENAME = "database.db"
conn = None

def reset_db():
	with open("sql/init.sql") as f:
		data = f.read().strip()
	curr = conn.cursor()
	print(data)
	curr.executescript(data)

def connect_or_create():
	needs_reset = not os.path.exists(DATABASE_FILENAME)
	global conn
	conn = sqlite3.connect(DATABASE_FILENAME)
	conn.row_factory = sqlite3.Row

	# Connect models
	db.DatabaseObject.connect(conn)
	ListContent.connect(conn)
	if needs_reset:
		reset_db()

if __name__ == '__main__':
	reset_db()