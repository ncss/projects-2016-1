import hashlib

from .list import List
from .db import DatabaseObject

def hashed_password(password):
  return hashlib.sha512(str(password).encode('utf-8')).hexdigest()

class User(DatabaseObject):
  def __init__(self, username, password, id=None):
    self.id = id
    self.username = username
    self.password = hashed_password(password)
    
  def to_dict(self):
    return {'username': self.username, 'password': self.password}

  def table_name(self):
    return 'users'

  def check_password(self, password):
    return self.password == hashed_password(password)

  def get_lists(self):
    return List.find_by_userid(self.id)

  @classmethod
  def find_username(cls, username):
    cur = DatabaseObject.conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=?', (username,))
    result = cur.fetchone()
    cur.close()
    return cls.from_row(result)

  @classmethod
  def authenticate(cls, username, password):
    hashed_pw = hashed_password(password)
    cur = DatabaseObject.conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=? AND password=?;', (username, hashed_pw))

    result = cur.fetchone()
    cur.close()
    return cls.from_row(result)
	


'''
if __name__ == '__main__':
  import sqlite3
  cn = sqlite3.connect('database.db')
  User.connect(cn)
  cn.row_factory = sqlite3.Row
  user = User.find_username('cool_hax4')
'''
