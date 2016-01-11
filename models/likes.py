class Likes:
  # Definitely needed to connect to database
  @staticmethod
  def connect(db):
    global conn
    conn = db

  def __init__(self,like_user, like_listnum, like_id):
    self.like_user = like_user
    self.like_listnum = like_listnum
    self.like_id = like_id
	

  
