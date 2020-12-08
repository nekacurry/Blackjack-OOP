from dealer import Dealer

class Player(Dealer):
  def __init__(self, name, deck, bust):
    super().__init__(deck, bust)
    self.name = name

  def display(self):
    for card in self.cards:
      print(card)
    print(f"Score: {self.get_score}")
