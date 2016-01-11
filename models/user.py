import hashlib

from .list import List
from .db import DatabaseObject


class User(DatabaseObject):
  def __init__(self, username, password, id=None):
    self.id = id
    self.username = username
    self.password = hashlib.sha512(str(password).encode('utf-8')).hexdigest() if not self.id else password
    
  def to_dict(self):
    return {'username': self.username, 'password': self.password}

  def table_name(self):
    return 'users'

  def check_password(self, password):
    return self.password == hashlib.sha512(str(password).encode('utf-8')).hexdigest()

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
    if username == "" or password == "":
      return None
    hashed_pw = hashlib.sha512(str(password).encode('utf-8')).hexdigest()
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
