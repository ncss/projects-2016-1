from .db import DatabaseObject

import sqlite3

class ListContent:
	@classmethod
	def connect(cls,db):
		cls.conn = db

	def __init__(self, list_id, item_order, content):
		self.content = content
		self.list_id = list_id
		self.item_order = item_order

	def __str__(self):
		return  '(' + self.content + ') Content, (' + str(self.list_id) + ') List, (' + str(self.item_order) + ') List position'

	def remove(self):
		self.__class__.delete(self.list_id, self.item_order)

	@classmethod
	def create(cls, list_id, item_order, content):
		cur = cls.conn.execute('''INSERT INTO list_contents VALUES (?, ?, ?)''', (list_id, item_order, content))
		cls.conn.commit()
		cur.close()
		return cls(list_id, item_order, content)

	@classmethod
	def delete(cls, list_id, item_order):
		cur = cls.conn.execute('''DELETE FROM list_contents WHERE list = ? AND item_order = ? ''', (list_id, item_order))
		cls.conn.commit()
		cur.close()

	@classmethod  
	def find(cls, content):
		cur = cls.conn.execute('''SELECT * FROM list_contents WHERE content=?''', (content,))
		row = cur.fetchone()
		if row is None:
			raise UserNotFound('{} does not exist'.format(content))
		return ListContent.helper(row)

	@classmethod
	def find_by_list_id(cls, list_id):
		cur = cls.conn.execute('''SELECT * FROM list_contents WHERE list=?''', (list_id,))
		rows = cur.fetchall()

		list = []
		for row in rows:
			item = ListContent.helper(row)
			list.append(item)

		return list

	@classmethod
	def search(cls,keyword):
		fuzzy_matcher = '%' + keyword + '%'
		cur = cls.conn.execute("""SELECT * FROM list_contents WHERE content LIKE ? """, ( fuzzy_matcher,))
		rows = cur.fetchall()

		list = []
		for row in rows:
			item = ListContent.helper(row)
			list.append(item)

		return list

	@classmethod
	def helper(cls, row):
		# to convert rows into named items
		list_id = row[0]
		item_order = row[1]
		content = row[2]
		return cls(list_id, item_order, content)

''' 
if __name__ == '__main__':
  conn = sqlite3.connect(':memory:')
  ListContent.connect(conn)
  conn.executescript(open('../sql/init.sql').read())
  print("Welcome to the ListContent module.")
  # create a new content item
  c = ListContent("test item 1",0,5)
  print(ListContent.findByListId(0))
  results = ListContent.search('movie')
  print(results)

  for r in results:
    print("Content: ", r.content)
'''
