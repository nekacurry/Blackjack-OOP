from card import Card
from deck import Deck
from hand import Hand
from dealer import Dealer
from player import Player

class Game:

  def __init__(self):
    pass

  def play(self):

    print("Welcome to Blackjack!")
    self.name = input("Please enter your name: ")
    print(self.name)

    self.display()
    if self.name == 'Dealer':
      while self.get_score() < 17:
        self.hit()
        self.display()
      self.check_for_bust()
    else:
