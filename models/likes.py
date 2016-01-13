from .db import DatabaseObject

class Likes(DatabaseObject):
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
    def remove(cls, user_id, list_id):
        cur = DatabaseObject.conn.cursor()
        cur = cls.conn.execute('DELETE FROM likes WHERE user_id=? AND list_id=?', (user_id, list_id))
        cur.close()

    @classmethod
    def list_likes(cls, list_id):
        cur = DatabaseObject.conn.cursor()
        cur = cls.conn.execute('SELECT COUNT(*) FROM likes WHERE list_id=?', (list_id,))
        res = cur.fetchone()
        cur.close()
        return res[0]

    def has_user_liked_list(self, user_id):
        cur = self.conn.cursor()
        cur.execute('SELECT COUNT(*) FROM likes WHERE user_id=? AND list_id=?', (int(user_id), self.id))
        res = cur.fetchone()
        cur.close()
        return res[0] == 1
