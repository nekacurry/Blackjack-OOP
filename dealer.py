from player import Player

class Dealer(Player):
  def __init__(self):
    super().__init__()
    self.cards = []
    self.value = 0

  def display(self):
    print("hidden")
    print(self.cards[1])
    

  

