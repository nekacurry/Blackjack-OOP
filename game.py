from card import Card
from deck import Deck
from dealer import Devil
from player import Player
import sys



class Game:
  def __init__(self):
    pass

#------------------------Hit Method--------------------------->
  def hit(self):

    choice = input("\nPress 'H' to Hit or a different key to Stand: ")
    print()

    if choice == 'h':
      self.player_hand.add_card(self.deck.deal())
      self.player_hand.display()
      if self.player_hand.get_value() > 21:
        print("\nYour soul just got BUSTED! You lose!")
        self.replay()
    else:
      print(self.stand())

#------------------------Stand Method--------------------------->
  def stand(self):
    player_hand = self.player_hand.get_value()
    devil_hand = self.devil_hand.get_value()

    print("~~~~~Results~~~~~")
    print("\n>> Your hand: ", player_hand)
    print(">> Devil's hand: ", devil_hand)
    print()

    if player_hand > devil_hand:
      print("\nYou Win! You get to keep your soul!")
      self.replay()
    elif player_hand == devil_hand:
      print("\nIt's a Tie! He beckons you to play again")
      self.replay()
    else:
      print("\nThe Devil Wins! Don't worry, Hell is lovely this time of year!")
      self.replay()

#------------------------Replay Method--------------------------->
  def replay(self):
    again = input("\nDare to tempt your fate again? [Y/N] ")
    if again.lower() == "n":
      sys.exit("\nHe'll get you next time!")
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
  def is_21(self, player_21, devil_21):
    '''strings for blackjack'''

    if player_21 and devil_21:
      print("\nIt's a Draw, but don't you wanna win? Go ahead, say yes.")

    elif player_21:
      print("\nBlackjack! Lucky you!")

    elif devil_21:
      print("\nDevil blackjack! C'mon, having a soul isn't THAT great.")
  

  #------------------------Play Method--------------------------->
  def play(self):
    playing = True

    while playing:
      print()
      print(' ,    ,    /\\   /\\')
      print('/( /\\ )\\  _\\ \\_/ /_')
      print('|\\_||_/| < \\_   _/ >')
      print('\\______/  \\|0   0|/')
      print('  _\\/_   _(_  ^  _)_')
      print( ' ( () ) /`\\|V"""V| /\\''')
      print('   {}   \\  \\_____/  /''')
      print('   ()   /\\   )=(   /\\''')
      print('   {}  /  \\_/\\=/\\_/  \\''')
      print('----------------------------->')
      print('------Devil\'s Blackjack------>')
      print('----------------------------->\n')

      self.deck = Deck()
      self.deck.shuffle()

      self.player_hand = Player()
      self.devil_hand = Devil()

      for _ in range(2):
        '''adds 2 cards to player deck'''

        self.player_hand.add_card(self.deck.deal())
        self.devil_hand.add_card(self.deck.deal())

      print(">> Your hand is: \n")
      self.player_hand.display()
      print("~~~~~~~~~~~~~~~~~~~~\n")
      print(">> The Devil draws: \n")
      self.devil_hand.display()
      print("~~~~~~~~~~~~~~~~~~~~")

      game_over = False

      while not game_over:
        '''checks for immediate blackjack'''
    
        player_21, devil_21 = self.check_21()

        if player_21 or devil_21:
          game_over = True
          self.is_21(
            player_21, devil_21)
          self.replay()

        else:
          self.hit()
      

#------------------------Call Game--------------------------->
if __name__ == "__main__":
    game = Game()
    game.play()