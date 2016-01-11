from .db import DatabaseObject

class List(DatabaseObject):

  def __init__(self, name, author, id = None):
    self.name = name
    self.author = author
    self.id = id

  def to_dict(self):
      return {'name':self.name, 'author':self.author}


  def table_name(self):
    return 'lists'


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
    cur.execute('SELECT * FROM lists where author=?', (uid,))
    results = cur.fetchall()
    cur.close()
    if not results: return None
    return [cls.from_row(i) for i in results]


  '''def  (self, ):
    cur = conn.cursor()
    con.execute(



  @staticmethod
  def find(self, limit):
    pass
'''
