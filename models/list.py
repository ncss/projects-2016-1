class List:
  def __init__(self, list, item_order):
    self.list = list
    self.item_order = item_order

  def find(self, id):
    cur = conn.cursor()
    cur.execute('select * FROM list WHERE id=?', (id,))

  '''def  (self, ):
    cur = conn.cursor()
    con.execute(
  

  
  @staticmethod
  def find(self, limit):
    pass
'''
