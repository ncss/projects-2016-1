def convert_row(row):
  keys = row.keys()
  return {key:row[idx] for idx,key in enumerate(keys)}

class List:
  @classmethod
  def connect(cls,db):
    cls.conn = db

  def __init__(self, list, item_order):
    self.list = list
    self.item_order = item_order

  @classmethod
  def find(cls, id):
    cur = cls.conn.cursor()
    cur.execute('SELECT * FROM lists WHERE id=?', (id,))

  @classmethod
  def find_by_userid(cls, uid):
    cur = cls.conn.cursor()
    cur.execute('SELECT * FROM list where author=?', (uid,))
    results = cur.fetchall()
    cur.close()
    return results

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
