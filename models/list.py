import sqlite3

class List:
  # Definitely needed to connect to database
  @staticmethod
  def connect(db):
    global conn
    conn = sqlite3.connect(db)
  
  def __init__(self, list, item_order):
    self.list = list
    self.item_order = item_order

  def find(self, id):
    cur = conn.cursor()
    findOb = cur.execute('select * FROM lists WHERE id=?', (id,))
    findLi = findOb.fetchall()
    return findLi[0]

  '''def  (self, ):
    cur = conn.cursor()
    con.execute(
  

  
  @staticmethod
  def find(self, limit):
    pass
'''
