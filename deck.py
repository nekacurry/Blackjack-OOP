from card import Card
import random

class Deck:

  def __init__(self):
    self.cards = [Card(suit, value) 
                  for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]
                  for value in ["A", "2", "3", "4", "5", "6",
                  "7", "8","9", "10", "J", "Q", "K"]] * 4
    self.shuffle()

  def shuffle(self):



    

    

