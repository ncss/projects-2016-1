class ListContent:
  # Definitely needed to connect to database
  @staticmethod
  def connect(db):
    global conn
    conn = db

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

  @staticmethod
  def findByListId(list_id):
    cur = conn.execute('''SELECT * FROM list_contents WHERE list=?''', (list_id,))
    rows = cur.fetchall()
      
    list = []
    for row in rows:
      item = ListContent(row[1],row[2],row[3])
      list.append(item)

    return list
  
  @staticmethod
  def search(keyword):
    
    fuzzy_matcher = '%' + keyword + '%'
    cur = conn.execute("""SELECT * FROM list_contents WHERE content LIKE ? """, ( fuzzy_matcher,))
    rows = cur.fetchall()

    list = []
    for row in rows:
      item = ListContent(row[1],row[2],row[3])
      list.append(item)

    return list
  
if __name__ == '__main__':
  conn = sqlite3.connect(':memory:')
  conn.executescript(open('../sql/init.sql').read())
  print("Welcome to the ListContent module.")
  # create a new content item
  c = ListContent("test item 1",0,5)
  print(ListContent.findByListId(0))
  results= ListContent.search('movie')
  print(results)

  for r in results:
    print("Content: ", r.content)
 
