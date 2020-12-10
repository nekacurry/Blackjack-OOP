from card import Card
from deck import Deck
from dealer import Devil
from player import Player



class Game:
  def __init__(self, game_over=False):
    self.game_over = game_over

#------------------------Hit Method--------------------------->
  def hit(self):
    '''the lower function turns uppercase letters in a string to lowercase
    for whatever reason, my code gave me an error when not using it
    would love some feedback as to why that happens!'''

    choice = input(("Press 'H' to Hit or a different key to Stand: ").lower())

    if choice == "h":
      self.player_hand.add_card(self.deck.deal())
      self.player_hand.display()
      if self.player_hand.get_value() > 21:
        print("Your soul just got BUSTED! You lose!")
        self.replay()
    else:
      print(self.stand())

#------------------------Stand Method--------------------------->
  def stand(self):
    player_hand = self.player_hand.get_value()
    devil_hand = self.devil_hand.get_value()

    print("~Results~")
    print("Your hand: ", player_hand)
    print("Devil's hand: ", devil_hand)

    if player_hand > devil_hand:
      print("You Win! You get to keep your soul!")
      self.replay()
    elif player_hand == devil_hand:
      print("It's a Tie! He beckons you to play again")
      self.replay()
    else:
      print("The Devil Wins! Don't worry, Hell is lovely this time of year!")
      self.replay()

#------------------------Replay Method--------------------------->
  def replay(self):
    again = input("Dare to tempt your fate again? [Y/N] ")
    if again.lower() == "n":
      print("He'll get you next time!")
    else:
      print(self.play())

#------------------------Check 21 Method--------------------------->
  def check_21(self):
    '''checks for blackjack'''

    player = False
    devil = False
    if self.player_hand.get_value() == 21:
        player = True
    if self.devil_hand.get_value() == 21:
        devil = True

    return player, devil

#------------------------21 Bool Method--------------------------->
  def is21(self, player_21, devil_21):
    '''strings for blackjack'''

    if player_21 and devil_21:
      print("It's a Draw, but don't you wanna win? Go ahead, say yes.")

    elif player_21:
      print("Blackjack! Luck you!")

    elif devil_21:
      print("Devil blackjack! C'mon, having a soul isn't THAT great.")
  

  #------------------------Play Method--------------------------->
  def play(self):
    playing = True

    while playing:
      print('---------------------------------------------')
      print('-------------Devil\'s Blackjack---------------')
      print('---------------------------------------------')

      self.deck = Deck()
      self.deck.shuffle()

      self.player_hand = Player()
      self.devil_hand = Devil()

      for _ in range(2):
        '''adds 2 cards to player deck'''

        self.player_hand.add_card(self.deck.deal())
        self.devil_hand.add_card(self.deck.deal())

      print("Your hand is: ")
      self.player_hand.display()
      print()
      print("Devil's hand is: ")
      self.devil_hand.display()

      game_over = False

      while not game_over:
        '''checks for immediate blackjack'''
    
        player_21, devil_21 = self.check_21()

        if player_21 or devil_21:
          game_over = True
          self.is21(
              player_21, devil_21)

        else:
          self.hit()
      

#------------------------Call Game--------------------------->
if __name__ == "__main__":
    game = Game()
    game.play()