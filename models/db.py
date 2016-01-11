def convert_row(row):  # common in other files
  keys = row.keys()
  return {key:row[idx] for idx,key in enumerate(keys)}

class DatabaseObject:

  @classmethod
  def connect(cls,db): 
    cls.conn = db
    
  @classmethod
  def from_row(cls,row):  
    if row is None: return None
    row = convert_row(row)
    return cls(**row)

  def to_dict(self):
      raise Exception('need to implement to_dict()')

  def save(self):  
    raw_data = self.to_dict()
    keys = raw_data.keys()
    values = list(raw_data.values())
    cur = self.__class__.conn.cursor()
    if not self.id:
      li = []
      for i in range(len(keys)):
        li.append('?')
      cur.execute('INSERT INTO users ({}) VALUES ({});'.format(",".join(keys),','.join(li)), values)
      self.id = cur.lastrowid
    else:
      li = []
      for i in keys:
        li.append(i + ' =?')
      values.append(self.id)
      cur.execute('''
        UPDATE users
        SET {}
        WHERE id = ?
      '''.format(','.join(li)), values);
    self.__class__.conn.commit()
    cur.close()
