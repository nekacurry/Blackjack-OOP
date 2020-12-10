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

    '''prints the second card drawn'''
    print(self.cards[1])
    

  

