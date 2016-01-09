from lib import ORM
import hashlib

class User:
  def __init__(self,username,password,name,email):
    self.username = username
    self.password = password
    self.email = email
  
  def check_password(self,password):
    return self.password == hashlib.sha512(password).hexdigest()  

  @staticmethod
  def find(username):
    cur = conn.cursor()
    
  @staticmethod
  def authenticate(username,password):
    cur = conn.cursor()
