class Likes:

    @classmethod
    def connect(cls, db):
        cls.conn = db

    def __init__(self, user_id, list_id):
      self.user_id = user_id
      self.list_id = list_id
