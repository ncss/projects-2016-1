
import sqlite3


class ListContent:
  @classmethod
  def connect(cls,db):
    cls.conn = db
  

  def __init__(self, content, list_num, item_order):
    self.content = content
    self.list_num = list_num
    self.item_order = item_order
    

  @classmethod
  def create(cls, content, list_num, item_order):
    cur = conn.execute('''INSERT INTO users VALUES (NULL,?, ?, ?)''', (content, list_num, item_order))
    return cls(content, list_num, item_order)

    

  @classmethod  
  def find(cls, content):
    cur = cls.conn.execute('''SELECT * FROM list_contents WHERE content=?''', (content,))
    row = cur.fetchone()
    if row is None:
      raise UserNotFound('{} does not exist'.format(content))
    return ListContent(row[0], row[1], row[2])

  @classmethod
  def findByListId(cls, list_id):
    cur = cls.conn.execute('''SELECT * FROM list_contents WHERE list=?''', (list_id,))
    rows = cur.fetchall()
      
    list = []
    for row in rows:
      item = ListContent(row[1],row[2],row[3])
      list.append(item)

    return list
  
  @classmethod
  def search(cls,keyword):
    
    fuzzy_matcher = '%' + keyword + '%'
    cur = cls.conn.execute("""SELECT * FROM list_contents WHERE content LIKE ? """, ( fuzzy_matcher,))
    rows = cur.fetchall()

    list = []
    for row in rows:
      item = ListContent(row[1],row[2],row[3])
      list.append(item)

    return list
  
if __name__ == '__main__':
  conn = sqlite3.connect(':memory:')
  ListContent.connect(conn)
  conn.executescript(open('../sql/init.sql').read())
  print("Welcome to the ListContent module.")
  # create a new content item
  c = ListContent("test item 1",0,5)
  print(ListContent.findByListId(0))
  results= ListContent.search('movie')
  print(results)

  for r in results:
    print("Content: ", r.content)
 
