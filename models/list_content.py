import sqlite3



class ListContent:
  def __init__(self, content, list_num, item_order):
    self.content = content
    self.list_num = list_num
    self.item_order = item_order
    
  
  @staticmethod  
  def find(content):
    cur = conn.execute('''SELECT * FROM list_contents WHERE content=?''', (content,))
    row = cur.fetchone()
    if row is None:
      raise UserNotFound('{} does not exist'.format(content))
    return ListContent(row[0], row[1], row[2])

  def findByListId(list_id):
    cur = conn.execute('''SELECT * FROM list_contents WHERE list=?''', (list_id,))
    rows = cur.fetchall()
    for row in rows:
      print(row)
      #item= ListContent
      
    return []

if __name__ == '__main__':
  conn = sqlite3.connect(':memory:')
  conn.executescript(open('../sql/init.sql').read())
  print("Welcome to the ListContent module.")
  # create a new content item
  c = ListContent("test item 1",0,5)
  ListContent.findByListId(0)
  

