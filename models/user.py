import hashlib

import db

class User(db.DatabaseObject):



  def __init__(self, username, password, id=None):
    self.id = id
    self.username =username
    self.password = password

  def to_dict(self):
    return {'username': self.username, 'password': self.password}
    


  def check_password(self,password):
    return self.password == hashlib.sha512(str(password).encode('utf-8')).hexdigest()

  def hash_password(self,password):
    self.password = hashlib.sha512(str(password).encode('utf-8')).hexdigest()

  def get_lists(self):
    pass


  @classmethod
  def find_username(cls,username):
    cur = cls.conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=?', (username,))
    result = cur.fetchone()
    cur.close()
    return cls.from_row(result)

  @classmethod
  def authenticate(cls,username,password):
    hashed_pw = hashlib.sha512(str(password).encode('utf-8')).hexdigest()
    cur = cls.conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=? AND password=?;', (username,hashed_pw))

    result = cur.fetchone()
    cur.close()
    return cls.from_row(result)

if __name__ == '__main__':
  import sqlite3
  cn = sqlite3.connect('database.db')
  User.connect(cn)
  cn.row_factory = sqlite3.Row
  user = User.find_username('cool_hax4')
  
