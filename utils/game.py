#card.py
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

#############################################
#player.py
#from card.py import Card
from random import choice as rndchoice
from random import shuffle as rndshuffle

        
class Player:
    
    def __init__(self,playername):
        self.turn_count=0
        self.playername=playername
        self.cards=[] #is a list of my `Card`
        self.number_of_cards=0 #is an int starting at 0
        self.history=[] #list of `Card` that will contain all the cards played by the player.

    def play(self):
        if self.cards == []:
            return False
        self.turn_count+=1
        card_picked=rndchoice(self.cards)
        self.history.append(card_picked)
        print(f'{self.playername} {self.turn_count} played: {card_picked.value} {card_picked.icon}')
        #should remove the played card!!???
        self.cards.remove(card_picked)
        
        return card_picked
        
class Deck:
    
    def __init__(self):
        self.cards = [] #a list of instances of `Card`
    
    #fill `cards` with a complete card game
    def fill_deck(self):
        for value in ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            for icon in ['♥', '♦', '♣', '♠']:
                self.cards.append(Card(value,icon))
        
    #shuffle all the list of `cards`
    def shuffle(self):
        rndshuffle(self.cards)
        
    #distribute the cards evenly between all the players.
    def distribute(self,deck_players):

        number_of_players=len(deck_players)
        nxt_card=0
       
        for i in self.cards:
        
            if ((52 - nxt_card) < number_of_players):
                #print("BREAKKKKKKKKKKKKKKKK")
                break
            
            for deck_player in deck_players:
                #print('------------------------------')
                #print("player:",deck_player.playername,deck_player)
                #check if enough cards available for distribution
    
                
                deck_player.cards.append(self.cards[nxt_card])

               
                nxt_card+=1
                #no more cards left
                if nxt_card == 52:
                    break
        #print("DEBUGwww::",deck_player.cards[2].value)
'''
        for i in deck_players:
            for j in i.cards:
                print("###############################")
                print("player:",i.playername)
                print("cards:",j.value,j.icon)

 '''

#########################################################################
#game.py
#from player.py import Player
class Board:
    def __init__(self,players):
        #list of Player
        self.players=players
        self.turn_count=0
        self.active_cards=[] #last card played by each player
        self.history_cards=[]
        #print('@@@@@@@@@@@@',len(self.players))
    
    def start_game(self):
        deck=Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)
        
        #play a card
        cardpicked=True
        self.active_cards=[]
        while cardpicked != False:
            self.history_cards+=self.active_cards
            self.active_cards=[]
            self.turn_count+=1
            for board_player in self.players:
                cardpicked=board_player.play()
                
                #print("cardpicked",cardpicked.value,cardpicked.icon,board_player.playername)
                if cardpicked == False:
                    print("NOMORECARDS!!!")
                    break
                self.active_cards.append(cardpicked)
                
            print(f'Turncount : {self.turn_count}     Number of cards in history : {len(self.history_cards)}')
            for i in self.active_cards:
                print("Active card are : ", i.value,i.icon)
            print('------------------------------------------------------------------------------')
        print("AFTERWHILEFINISHED")
        
class Inviteplayers:
    def __init__(self):
        self.players=[]
        while True:
            new_player=input("Enter your name :")
            if new_player == '':
                break
            self.players.append(Player(new_player))
        #print("@@##@@##",len(self.players))
        



#MAIN
######
zz=Board(Inviteplayers().players)

zz.start_game()
