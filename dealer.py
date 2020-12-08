from hand import Hand

class Dealer(Hand):
  def __init__(self, name, deck):
    super().__init__()
    self.name = 'Dealer'
    self.deck = deck
    self.bust = False

  def show_hand(self):
    for card in self.score:
      print(card),
    print

  def stand(self):
    print(f"{self.name} stands with {self.score}")

  def hit(self):
    self.draw_card(self.deck.deal_card())
    print(f"{self.name} hits")
    return self.cards

  def check_for_bust(self):
    if self.calculate_score() > 21:
      self.bust = True
      print(f"{self.name} gets bust")