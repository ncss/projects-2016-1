class Likes:

# Both init and create defs mirrored on list_content methods - need checking
    def __init__(self, like_user, like_listnum):
        self.like_user = like_user
        self.like_listnum = like_listnum

    @classmethod
    def connect(cls, db):
        cls.conn = db

    @classmethod
    def create(cls, user_id, list_id):
        cur = cls.conn.execute('INSERT INTO likes VALUES (NULL, ?, ?)', (user_id, list_id))

    @classmethod
    def list_likes(cls, list_id):
        cur = cls.conn.execute('SELECT COUNT(*) FROM likes WHERE list_id=?', list_id)
        return cur.fetchone()

    @classmethod
    def has_user_liked_list(cls, user_id, list_id):
        cur = cls.conn.execute('SELECT COUNT(*) FROM likes WHERE list_id=?, user_id=?', list_id, user_id)
        if cur.fetchone() == 1:
            return True
        else:
            return False

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
	#  return [cls.from_row(i) for i in results]
'''
=======
>>>>>>> origin/master
'''
