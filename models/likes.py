class Likes:
  # Definitely needed to connect to database
  @staticmethod
  def connect(db):
    global conn
    conn = db

  def __init__(self):
    pass

  
