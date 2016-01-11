from .db import DatabaseObject
from .list_content import ListContent

class List(DatabaseObject):
  def __init__(self, name, author, id = None):
    self.name = name
    self.author = author
    self.id = id

  def to_dict(self):
      return {'name': self.name, 'author': self.author}

  def table_name(self):
    return 'lists'

  def list_contents(self):
    return ListContent.find_by_list_id(self.id)

  def get_likes(self):
    cur = self.conn.cursor()
    cur.execute('SELECT COUNT(*) FROM likes WHERE list_id=?', (self.id,))
    result = cur.fetchone()
    return result[0]

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
    if not results: return []
    return [cls.from_row(i) for i in results]

  @classmethod
  def find_all(cls):
    cur = cls.conn.cursor()
    cur.execute('SELECT * FROM lists')
    results = cur.fetchall()
    cur.close()
    if not results: return []
    return [cls.from_row(i) for i in results]


  '''def  (self, ):
    cur = conn.cursor()
    con.execute(



  @staticmethod
  def find(self, limit):
    pass
'''
