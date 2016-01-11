class Likes:
  # Definitely needed to connect to database
  @staticmethod
  def connect(db):
    global conn
    conn = db

# Both init and create defs mirrored on list_content methods - need checking
	
  def __init__(self,like_user, like_listnum, like_id):
    self.like_user = like_user
    self.like_listnum = like_listnum
    self.like_id = like_id
	
  @classmethod
  def create(cls, like_user, like_listnum, like_id):
    #like_id is an autonumber field, how does inserting work? insert a null?
	cur = conn.execute('''INSERT INTO likes VALUES (NULL,?, ?, ?)''', (like_id, like_user, like_listnum))
    return cls('Created: like_id ?, like_user ?, like_listnum ?', like_id, like_user, like_listnum)

'''	WORKS IN PROGRESS
  @classmethod
  def find(cls, list):
    """Gets all authors who liked a list ID
	Should it also return author names?
    """
    cur = cls.conn.cursor()
    cur.execute('SELECT person FROM likes WHERE list=?', (list,))
    result = cur.fetchone()
    return cls.from_row(result)

  @classmethod
  def find_by_userid(cls, uid):
    """Gets all likes for an author
	Return the list ID from the likes table
	Should it also return the list name from the lists table?
	"""
	cur = cls.conn.cursor()
    cur.execute('SELECT * FROM list where author=?', (uid,))
    results = cur.fetchall()
    cur.close()
    if not results: return None
    return [cls.from_row(i) for i in results]
'''