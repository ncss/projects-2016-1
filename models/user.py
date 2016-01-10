
import sqlite3
conn = sqlite3.connect("database.db")
conn.row_factory = sqlite3.Row

import hashlib

def convert_row(row):
  keys = row.keys()

  return {key:row[idx] for idx,key in enumerate(keys)}


class User:
  def __init__(self,saved=False,**kwargs):
    self.username = kwargs["username"]
    self.password = kwargs["password"]
    self.saved = saved
    

  def check_password(self,password):
    return self.password == hashlib.sha512(str(password).encode('utf-8')).hexdigest()
	
  def get_lists(self):
    pass

  def save(self):
    cur = con.cursor()
    if not self._saved:
      cur.execute('INSERT INTO users (username,password,email)VALUES=(?,?,?);', (self.username,self.password,self.email));
    else:
      cur.execute('''
        UPDATE users
        SET username=?,
            password=?,
            email=?
      ''',(self.username,self.password,self.email));
    conn.commit()
    cur.close()
  
  @staticmethod
  def findUsername(username):
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=?', (self.username))
    return User(cur.fetchone())
    cur.close()
  
  @staticmethod
  def new_user(self, *args):
    pass

  @staticmethod
  def authenticate(username,password):
    hashed_pw = hashlib.sha512(str(password).encode('utf-8')).hexdigest()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=? AND password=?;', (username,hashed_pw))

    result = cur.fetchone()
    cur.close() 
    if result is None: return False
    result = convert_row(result)
    return User(saved=True,**result)


