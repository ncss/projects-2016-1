class ORM:
  def __init__(self):
    pass
  
  def save(self):
    table_name = self.__class__.__name__.lower()+"s"
    cur = conn.cursor()
    if self._saved:
      cur.execute()
    else:
      cur.execute('INSERT into {} ()'.format(table_name),())
    conn.commit()
    cur.close()
  
  @staticmethod
  def find(id):
    table_name = self.__class__.__name__.lower()+"s"
    cur = conn.cursor()
    cursor.execute('''SELECT * FROM ? WHERE id=?''',(table_name,id))
