
class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

#------------------------Repr Method--------------------------->
  '''returns suit/value into a proper string'''
  def __repr__(self):
    return " of ".join((self.value, self.suit))
