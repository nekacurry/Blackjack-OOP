from card import Card
from deck import Deck
from hand import Hand
from dealer import Dealer
from player import Player


def play(player, deck):
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

def report(player, dealer):
    if player.bust:
      print("You Busted! It's a Loss!")
    elif len(player.hand) == 2 and player.get_score() == 21:
      print("Blackjack! You Win!")
    elif dealer.bust:
      print("Dealer Busted! You Win!")
    elif (player.get_score() > dealer.get_score()):
      print("You Win!")
    elif player.get_score() == dealer.get_score():
      print("It's a Tie!")
    else:
      print("Sorry, Dealer Wins!")


def game():

  dealer = Dealer('Dealer', deck, bust)
  deck = Deck()
  player = Player(input("Please enter your name: ")


  for player in (players + dealer):
    player.draw_card(deck.deal())
    play(player, deck)
    print

if __name__ == '__main__':
  game()



