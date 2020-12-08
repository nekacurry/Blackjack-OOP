from card import Card

class Hand:
  
  def __init__(self, dealer):
    self.cards = []
    self.dealer = dealer
    self.score = 0

  def draw_card(self, card):
    self.cards.append(card)
