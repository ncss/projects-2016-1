import sqlite3
import hashlib

conn = sqlite3.connect("database.db")

cur = conn.cursor()
for i in range(100):
  cur.execute('''INSERT INTO users (username,password)
                VALUES (?,?);''',("User"+str(i),hashlib.sha512(str("pw"+str(i)).encode('utf-8')).hexdigest()));
conn.commit()
