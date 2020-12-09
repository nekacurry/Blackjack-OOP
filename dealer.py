from hand import Hand
from deck import Deck

class Dealer(Hand):
  def __init__(self, name, deck, bust=False):
    Hand.__init__(self)
    self.name = 'Dealer'
    self.deck = deck
    self.bust = bust

  def show_hand(self):
    for card in self.cards:
      print(card)
    print

  def stand(self):
    print(f"{self.name} stands with {self.score}")

  def hit(self):
    self.draw_card(self.deck.deal())
    print(f"{self.name} hits")
    return self.cards

  def check_for_bust(self):
    if self.calculate_score() > 21:
      self.bust = True
      print(f"{self.name} gets bust")
    else:
      self.stand()

  def display(self):
    print(self.cards)

