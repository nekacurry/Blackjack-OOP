from card import Card

class Player():
  def __init__(self, name='Mortal'):
    self.cards = []
    self.value = 0
    self.name = name

#------------------------Add Card Method--------------------------->
  def add_card(self, card):
    '''puts a hit card on the end of card list'''

    self.cards.append(card)

#------------------------Calculate Value Method--------------------------->
  def calculate_value(self):
    self.value = 0
    is_ace = False
    for card in self.cards:
      if card.value.isnumeric():
        self.value += int(card.value)
        '''using isnumeric to determine if card value is a number, 
          if so, turns numeral to int and adds to score'''
          
      else:
        '''Aces count as 11, all other face cards count as 10'''

        if card.value == "A":
          is_ace = True
          self.value += 11
        else:
          self.value += 10

    if is_ace and self.value > 21:

      '''Aces count as a 1 if the player would otherwise bust.
      this if statement adjusts the score in response'''
      self.value -= 10

#------------------------Get Value Method--------------------------->
  def get_value(self):
    self.calculate_value()
    return self.value   

#------------------------Display Method--------------------------->
  def display(self):
    for card in self.cards:
      print(card)
    print("Value:", self.get_value())