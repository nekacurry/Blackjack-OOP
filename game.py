from card import Card
from deck import Deck
from dealer import Dealer
from player import Player


class Game:
  def __init__(self):
    pass

  def play(self):
    playing = True

    while playing:
      self.deck = Deck()
      self.deck.shuffle()

      self.player_hand = Player()
      self.dealer_hand = Dealer()

      for _ in range(2):
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

      print("Your hand is:")
      self.player_hand.display()
      print()
      print("Dealer's hand is:")
      self.dealer_hand.display()

      game_over = False

      while not game_over:
        player_21, dealer_21 = self.check_21()
        if player_21 or dealer_21:
          game_over = True
          self.results(
              player_21, dealer_21)
          continue
      
        choice = input(("Please choose [Hit / Stand] ").lower())
        while choice not in ["h", "s", "hit", "stand"]:
          choice = input("Please enter 'hit' or 'stand' (or H/S) ").lower()

        if choice in ['hit', 'h']:
          self.player_hand.add_card(self.deck.deal())
          self.player_hand.display()
          if self.player_is_over():
            print("You busted! You lose!")
            game_over = True

        else:
          player_hand = self.player_hand.get_value()
          dealer_hand = self.dealer_hand.get_value()

          print("~Results~")
          print("Your hand:", player_hand)
          print("Dealer's hand:", dealer_hand)

          if player_hand > dealer_hand:
            print("You Win!")
          elif player_hand == dealer_hand:
            print("It's a Tie!")
          else:
            print("Dealer Wins!")
          game_over = True

      again = input("Play Again? [Y/N] ")
      if again.lower() == "n":
        print("Thanks for playing!")
        playing = False
      else:
        game_over = False

  def check_21(self):
    player = False
    dealer = False
    if self.player_hand.get_value() == 21:
        player = True
    if self.dealer_hand.get_value() == 21:
        dealer = True

    return player, dealer

  def results(self, player_21, dealer_21):
    if player_21 and dealer_21:
      print("It's a Draw!")

    elif player_21:
      print("Blackjack! You win!")

    elif dealer_21:
      print("Dealer blackjack! Dealer wins!")

  def player_is_over(self):
    return self.player_hand.get_value() > 21


if __name__ == "__main__":
    game = Game()
    game.play()