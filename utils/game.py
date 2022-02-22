
#########################################################################
#game.py
from player import Player, Deck
from card import Card
class Board:
    def __init__(self,players: [Player]):
 
        self.players: [Player] = players
        self.turn_count: int = 0
        self.active_cards: [Card] = [] #last card played by each player
        self.history_cards: [Card] = []
    
    def start_game(self):
        deck=Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)
        
        #play a card
        #self.active_cards=[]
        while True:
            self.history_cards+=self.active_cards
            self.active_cards=[]
            #self.turn_count+=1
            for board_player in self.players:
                cardpicked=board_player.play()                
                if cardpicked == []:
                    #print("NOMORECARDS!!!")
                    break
                self.active_cards.append(cardpicked)
            if cardpicked == []:
                break
            self.turn_count+=1 
             
            print(f'Turncount : {self.turn_count}     Number of cards in history : {len(self.history_cards)}')
            for i in self.active_cards:
                print("Active cards are : ", i.value,i.icon)
            print('------------------------------------------------------------------------------')

from typing import Union   ,List 
class Inviteplayers:
    def __new__(self) -> Union[bool,List [Player]]:
        self.players: [Player] = []
        plyer=0
        while True:
            plyer+=1
            new_player=input(f"Player {plyer} enter your name (Return to finish!) : ")
            if new_player == '' and plyer == 1:
                return False
            elif new_player == '':
                break #Finished input of players
            self.players.append(Player(new_player))
        return(self.players)


