from player import Player

class Devil(Player):
  def __init__(self, name='Devil'):
    super().__init__(name)
    self.cards = []
    self.value = 0
    self.name = name

  def display(self):
    print("hidden")
    print(self.cards[1])
    

  

