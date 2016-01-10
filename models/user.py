from lib import ORM
import hashlib

class User(ORM.ORM):
  def __init__(**kwargs,saved=False):
    self.username = username
    self.password = password
    self.email = email
    self._saved = saved

  def check_password(self,password):
    return self.password == hashlib.sha512(password).hexdigest()
	
  def new_list(self):
    pass

  @staticmethod
  def find(username):
    cur = conn.cursor()

  @staticmethod
  def new_user(self, *args):
    pass

  @staticmethod
  def authenticate(username,password):
    hashed_pw = hashlib.sha512(password).hexdigest()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=? AND password=?',(username,hashed_pw))

    result = cur.fetchone()
    if result is None: return False
    return User(**result,saved=True)

