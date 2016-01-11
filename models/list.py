import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()


def convert_row(row):
  keys = row.keys()
  return {key:row[idx] for idx,key in enumerate(keys)}

class List:
  @classmethod
  def connect(cls,db):
    cls.conn = db

  def __init__(self, list_name, list_author, list_id = none):
    self.list = list
    self.item_order = item_order

  @classmethod
  def find(cls, id):
    """Gets a list by ID
    """
    cur = cls.conn.cursor()
    cur.execute('SELECT * FROM lists WHERE id=?', (id,))
    result = cur.fetchone()
    return cls.from_row(result)

  @classmethod
  def find_by_userid(cls, uid):
    cur = cls.conn.cursor()
    cur.execute('SELECT * FROM list where author=?', (uid,))
    results = cur.fetchall()
    cur.close()
    if not results: return None
    return [cls.from_row(i) for i in results]

  @classmethod
  def from_row(cls,row):
    if row is None: return None
    row = convert_row(result)
    return cls(saved=True,**row)


  '''def  (self, ):
    cur = conn.cursor()
    con.execute(



  @staticmethod
  def find(self, limit):
    pass
'''
