from player import Player

class Devil(Player):
  def __init__(self, name='Satan'):

    '''inherits attributes from Player class'''
    super().__init__()
    self.cards = []
    self.value = 0
    self._name = name

#------------------------Display Method--------------------------->
  def display(self):
    print("*** SECRET ***")

    devil_list = self.cards[1:5]
    '''prints starting from the second card drawn'''
    print(*devil_list, sep="\n")
    '''puts each item in list on new line'''
    

  

