class ListContent:
  def __init__(self, content, list_num, item_order):
    self.content = content
    self.list_num = list_num
    self.item_order = item_order
    
  
  @staticmethod  
  def find(description):
    pass


if __name__ == '__main__':
  print("Welcome to the ListContent module.")
  # create a new content item
  c = ListContent("test item 1")
  

