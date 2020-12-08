from card import Card

class Hand:
  
  def __init__(self):
    self.cards = []
    self.score = 0

  def draw_card(self, card):
    self.cards.append(card)

  def calculate_score(self): 
    self.score = 0
    ace = False

    if ace and self.score > 21:
      self.score -= 10

    for card in self.cards:
      if card.value.isnumeric():
        self.score += int(card.value)
      else:
        if card.value == "A":
          ace = True
          self.score += 11
        else:
          self.score += 10
    
    
  def show_score(self):
    self.calculate_score()
    return self.score