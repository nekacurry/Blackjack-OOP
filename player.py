from dealer import Dealer
from hand import Hand

class Player(Dealer):
  def __init__(self, name, deck, bust):
    super().__init__(deck, bust)
    self.name = name
    self.deck = deck
    self.bust = bust

  def display(self):
    for card in self.cards:
      print(card)
    print(f"Your Score: {self.get_score}")
