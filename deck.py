from card import Card
import random

class Deck:

  def __init__(self):

    '''card names and values are multiplied by 4 so it's the standard probability to a real deck'''
    self.cards = [Card(suit, value) 
                  for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]
                  for value in ["A", "2", "3", "4", "5", "6",
                  "7", "8","9", "10", "J", "Q", "K"]] * 4

#------------------------Shuffle Method--------------------------->
  def shuffle(self):
    '''randomizes cards'''

    random.shuffle(self.cards)
  
#------------------------Deal Method--------------------------->
  def deal(self): 
    '''adds card to player class's card list'''

    if len(self.cards) > 1:
      return self.cards.pop()

  



    

    

