import sqlite3
import hashlib

conn = sqlite3.connect("../database.db")

cur = conn.cursor()

with open('names.txt') as f:

  for i in f:
    i = i.lower().strip().split()
    cur.execute('''INSERT INTO users (username,password)
                VALUES (?,?);''',(i[0]+"_"+i[1],hashlib.sha512(str(i[0]+i[1]).encode('utf-8')).hexdigest()));

conn.commit()
