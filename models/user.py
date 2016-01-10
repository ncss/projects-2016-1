import hashlib

def convert_row(row):
  keys = row.keys()
  return {key:row[idx] for idx,key in enumerate(keys)}


class User:

  @staticmethod
  def connect(db):
    global conn
    conn = db

  def __init__(self,saved=False,**kwargs):
    self.username = kwargs["username"]
    self.password = kwargs["password"]
    self._saved = saved
    

  def check_password(self,password):
    return self.password == hashlib.sha512(str(password).encode('utf-8')).hexdigest()

  def hash_password(self,password):
    self.password = hashlib.sha512(str(password).encode('utf-8')).hexdigest()
	
  def get_lists(self):


  def save(self):
    cur = conn.cursor()
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
  def from_row(row):
    if result is None: return None
    result = convert_row(result)
    return User(saved=True,**result)

  @staticmethod
  def find_username(username):
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=?', (self.username))
    result = cur.fetchone()
    cur.close()
	return User.from_row(result)

  @staticmethod
  def authenticate(username,password):
    hashed_pw = hashlib.sha512(str(password).encode('utf-8')).hexdigest()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=? AND password=?;', (username,hashed_pw))

    result = cur.fetchone()
    cur.close() 
    return User.from_row(result)

