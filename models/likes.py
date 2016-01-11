from .db import DatabaseObject

class Likes(DatabaseObject):

# Both init and create defs mirrored on list_content methods - need checking
    def __init__(self, user_id, list_id):
        self.like_user = user_id
        self.list_id = list_id

    @classmethod
    def connect(cls, db):
        cls.conn = db

    @classmethod
    def create(cls, user_id, list_id):
        cur = DatabaseObject.conn.cursor()
        cur = cls.conn.execute('INSERT INTO likes VALUES (NULL, ?, ?)', (user_id, list_id))
        cur.close()

    @classmethod
    def list_likes(cls, list_id):
        cur = DatabaseObject.conn.cursor()
        cur = cls.conn.execute('SELECT COUNT(*) FROM likes WHERE list_id=?', list_id)
        res = cur.fetchone()
        cur.close()
        return res[0]

    @classmethod
    def has_user_liked_list(cls, user_id, list_id):
        cur = DatabaseObject.conn.cursor()
        cur = cls.conn.execute('SELECT COUNT(*) FROM likes WHERE list_id=?, user_id=?', list_id, user_id)

        res = cur.fetchone()
        cur.close()

        return res[0] == 1

''' WORKS IN PROGRESS
  @classmethod
  def find(cls, list):
    """Gets all authors who liked a list ID
    Should it also return author names?
    """
    cur = cls.conn.cursor()
    cur.execute('SELECT person FROM likes WHERE list=?', (list,))
    result = cur.fetchone()
    if not results:
      return None
    else:
      return cls.from_row(result)

  @classmethod
  def find_by_userid(cls, uid):
    """Gets all lists liked by an user
    Return the list ID from the likes table
    Should it also return the list name from the lists table?
    """
    cur = cls.conn.cursor()
    cur.execute('SELECT list FROM likes where person=?', (author,))
    results = cur.fetchall()
    cur.close()
    if not results:
      return None
    else:
      return [cls.from_row(i) for i in results]
'''
