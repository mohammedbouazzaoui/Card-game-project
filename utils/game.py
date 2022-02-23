# Project : challenge-card-game-becode
# FILE: game.py
#
# Author: Bouazzaoui M.
# Date: 23/02/2022
# Version: 1.0
#

from card import Card
from player import Player, Deck
from typing import Union   ,List 


class Board:
    """
    The class creates a Board object that holds all the necessary information
    about the game and allows to start the game.
    
    Inherited Classes
    -----------------
    none
    
    Attributes
    ----------
    players:            List of Player objects one for every player
    turn_count:         int turn counter
    active_cards:       List of Card objects with the now active cards
    history_cards:      List of Card objects with the history
    
    Methods:
    --------
    __init__    : Initializes the object.
    __str__     : Function that returns an information string of the object.
    start_game  : start the game
    """
    
    def __init__(self,players: List[Player]) -> None:
        """
        Init function that will initialize a Board.
        
        :param players: a list of Player objects
        """
        
        self.players: [Player] = players
        self.turn_count: int = 0
        self.active_cards: [Card] = [] #last card played by each player
        self.history_cards: [Card] = []
    
    def start_game(self) -> None:
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
                if cardpicked == None:
                    #print("NOMORECARDS!!!")
                    break
                self.active_cards.append(cardpicked)
            if cardpicked == None:
                break
            self.turn_count+=1 
             
            print(f'Turncount : {self.turn_count}     Number of cards in history : {len(self.history_cards)}')
            for i in self.active_cards:
                print("Active cards are : ", i.value,i.icon)
            print('------------------------------------------------------------------------------')

    def __str__(self) -> str:
        """
        Function that creates an information string of the object.
        
        :return: information string.
        """
        #self.players: [Player] = players
        #self.turn_count: int = 0
        #self.active_cards: [Card] = [] #last card played by each player
        #self.history_cards: [Card] = []
        info = f'Players:\n{self.playername} \ncards:{self.cards}\nturn_count:{self.turn_count} \nnumber_of_cards:{self.number_of_cards} \nhistory:{self.history_cards}\n'
        return info

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


a=Board()
print('@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@')
print(a)