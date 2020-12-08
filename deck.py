from card import Card
import random

class Deck:

  def __init__(self):
    self.deck = [Card(suit, value) 
                  for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]
                  for value in ["A", "2", "3", "4", "5", "6",
                  "7", "8","9", "10", "J", "Q", "K"]] * 4
    self.shuffle()

  def shuffle(self):
    random.shuffle(self.deck)
  
  def deal(self): 
    if len(self.deck) > 1:
      return self.deck.pop()

  



    

    

