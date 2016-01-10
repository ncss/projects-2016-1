import hashlib
from list import List

def convert_row(row):
  keys = row.keys()
  return {key:row[idx] for idx,key in enumerate(keys)}


class User:

  @classmethod
  def connect(cls,db):
    cls.conn = db

  def __init__(self, username, password, id=None):
    self.id = id
    self.username =username
    self.password = password

  def check_password(self,password):
    return self.password == hashlib.sha512(str(password).encode('utf-8')).hexdigest()

  def hash_password(self,password):
    self.password = hashlib.sha512(str(password).encode('utf-8')).hexdigest()

  def get_lists(self):
    return List.find_by_userid(cls, self.id)

  def save(self):
    cur = self.__class__.conn.cursor()
    if not self.id:
      cur.execute('INSERT INTO users (username,password) VALUES (?,?);', (self.username,self.password))
      self.id = cur.lastrowid
    else:

      cur.execute('''
        UPDATE users
        SET username=?,
            password=?
        WHERE id = ?
      ''',(self.username,self.password, self.id));
    self.__class__.conn.commit()
    cur.close()

  @classmethod
  def from_row(cls,row):
    if row is None: return None
    row = convert_row(row)
    return cls(saved=True,**row)

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
  user = User.find_username('cool_hax3')

