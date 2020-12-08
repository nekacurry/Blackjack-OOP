from card import Card
from deck import Deck
from hand import Hand
from dealer import Dealer
from player import Player

class Game(Player):

  def __init__(self):
    pass

  def play(self, player):

    print("Welcome to Blackjack!")
    player.name = input("Please enter your name: ")

    player.display()
    if player.name == 'Dealer':
      while player.get_score() < 17:
        player.hit()
        player.display()
      player.check_for_bust()

    else:
      choice = input("Would you like to Stand or Hit?: ")

    if choice == "Stand":
      player.stand()

    while choice == "Hit":
      player.hit()
      player.display()
      if player.get_score() > 21:
        player.bust = True
        print(f"{player.name} gets bust")
        break
      choice = input("Would you like to Hit again or Stand?: ")

play()