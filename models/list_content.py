
import sqlite3


class ListContent:
  @classmethod
  def connect(cls,db):
    cls.conn = db
  

  def __init__(self, list_num, item_order, content):
    self.content = content
    self.list_num = list_num
    self.item_order = item_order
    
  def __str__(self):
    return  '(' + self.content + ') Content, (' + str(self.list_num) + ') List, (' + str(self.item_order) + ') List position'
	
  @classmethod
  def create(cls, list_num, item_order, content):
    cur = conn.execute('''INSERT INTO list_contents VALUES (?, ?, ?)''', (list_num, item_order, content))
    return cls(list_num, item_order, content)

    

  @classmethod  
  def find(cls, content):
    cur = cls.conn.execute('''SELECT * FROM list_contents WHERE content=?''', (content,))
    row = cur.fetchone()
    if row is None:
      raise UserNotFound('{} does not exist'.format(content))
    return ListContent.helper(row)

  @classmethod
  def findByListId(cls, list_id):
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
	list_num = row[0]
	item_order = row[1]
	content = row[2]
	return cls(list_num, item_order, content)
  
  
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
 
