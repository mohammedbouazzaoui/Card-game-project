
#import random

class Symbol:
    def __init__(self,icon):
        self.icon=icon #(['♥', '♦', '♣', '♠'])
        if icon == '♦' or icon == '♥':
            self.color='red'
        else:            
            self.color='black'  #['red','black']
        
class Card(Symbol):
    def __init__(self,value,icon):
        super().__init__(icon)
        self.value=value  #(['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K'])
        #self.icon=icon
        #self.color=color
        


#############################################


#from card.py import Card
from random import choice
from random import shuffle

        
class Player:
    #players=[] #alist of all players
    turn_counts=0
    #number_of_players=0
    
    def __init__(self,playername):
        #test 
        self.playername=playername
        #Player.players.append(self.playername)
        #Player.number_of_players+=1
        self.cards=[] #is a list of my `Card`
        #self.turn_count=0 #is an int starting a 0
        self.number_of_cards=0 #is an int starting at 0
        self.history=[] #list of `Card` that will contain all the cards played by the player.

    def play(self):
        #card_picked=random.choice(self.cards)
        card_picked=choice(self.cards)
        self.history+=card_picked
        print(f'{self.name} {self.turn_count} played: {card_picked.value} {card_picked.icon}')
        #should remove the played card!!???
        return card_picked
        
class Deck:
    
    def __init__(self):
        self.cards = [] #a list of instances of `Card`
    
    #fill `cards` with a complete card game
    def fill_deck(self):
        for value in ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            for icon in ['♥', '♦', '♣', '♠']:
                #zzz=Card(2,2)
                self.cards.append(Card(value,icon))
        
    #shuffle all the list of `cards`
    def shuffle(self):
        #random.shuffle(self.cards)
        shuffle(self.cards)
        
    #distribute the cards evenly between all the players.
    def distribute(self,players):
        print('@@@@@@@@@',type(players))
        number_of_players=len(players)
        nxt_card=0
        for player in players:
            #check if enough cards available for distribution
            if ((52 - nxt_card) < number_of_players):
                break
            player.cards.append(self.cards[nxt_card])
            nxt_card+=1
            #no more cards left
            if nxt_card == 52:
                break
        

   

#########################################################################



'''
In `game.py` create:

A class called `Board` that contains:

- An attribute `players` that is a list of `Player`. It will contain all the players that are playing.
- An attribute `turn_count` that is an int.
- An attribute `active_cards` that will contain the last card played by each player.
- An attribute `history_cards` that will contain all the cards played since the start of the game, except for `active_cards`.
- A method `start_game()` that will:
  - Start the game,
  - Fill a `Deck`,
  - Distribute the cards of the `Deck` to the players.
  - Make each `Player` `play()` a `Card`, where each player should only play 1 card per turn, and all players have to play at each turn until they have no cards left.
  - At the end of each turn, print:
    - The turn count.
    - The list of active cards.
    - The number of cards in the `history_cards`.
'''

#from player.py import Player




class Board:
    def __init__(self,players):
        #list of Player
        self.players=players
        self.turn_count=0
        self.active_cards=[] #last card played by each player
    
    def start_game(self):
        deck=Deck()
        #input("/1@@@@@@@@@@@@@@@@@@@@@@@@@@")
        deck.fill_deck()
        #input("/2@@@@@@@@@@@@@@@@@@@@@@@@@@")
        deck.shuffle()
        print(deck.cards[0].value,deck.cards[0].icon)
        print(deck.cards[1].value,deck.cards[1].icon)
        print(deck.cards[51].value,deck.cards[51].icon)
        #input("/3@@@@@@@@@@@@@@@@@@@@@@@@@@")
        deck.distribute(list(self.players))
        input("/4@@@@@@@@@@@@@@@@@@@@@@@@@@")
    


     

class Inviteplayers:
    def __init__(self):
        self.players=[]
        while True:
            new_player=input("Enter your name :")
            if new_player == '':
                break
            self.players.append(Player(new_player))
        print("@@##@@##",len(self.players))
        
#z=Inviteplayers()
#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",z.players)
#print(players)
zz=Board(Inviteplayers())

zz.start_game()
