import sqlite3

conn = sqlite3.connect("database.db")

cur = conn.cursor()
for i in range(1000):
  cur.execute('''INSERT INTO users (username,password,name,email)
                VALUES (?,?,?,?);''',("User"+str(i),"pw"+str(i),"User "+str(i),"email"+str(i)+"@email.com"));

conn.commit()
