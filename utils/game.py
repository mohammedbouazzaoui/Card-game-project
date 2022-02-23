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
        
        self.players: List[Player] = players
        self.turn_count: int = 0
        self.active_cards: [Card] = [] #last card played by each player
        self.history_cards: [Card] = []
    
    def start_game(self) -> None:
        """
        Function that will 
        Start the game,
        Fill a Deck,
        Distribute the cards of the Deck to the players.
        Make each Player play() a Card, where each player should only 
        play 1 card per turn, and all players have to play at each turn 
        until they have no cards left.
        At the end of each turn a print is done of:
            The turn count.
            The list of active cards.
            The number of cards in the history_cards.
        """
        
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
             
            crds=''
            for actcrd in self.active_cards:
                crds=crds+f'{actcrd.value}{actcrd.icon} ,'
            print(f'Turn count: {self.turn_count}\nNumber of cards in history: \n{len(self.history_cards)}\nActive cards:\n{crds}')
            print('----------------')

    def __str__(self) -> str:
        """
        Function that creates an information string of the object.
        
        :return: information string.
        """

        allplayernames=''
        for n in self.players:
            allplayernames=allplayernames + n.playername + ', '
        info = f'Players:\n{allplayernames}\nTurn: {self.turn_count}\nCards:\n{self.active_cards}\nHistory:\n{self.history_cards}\n'
        return info

class Inviteplayers:
    """
    The class will just create a bunch of players.
    
    Inherited Classes
    -----------------
    none
    
    Attributes
    ----------
    players: a list of Player objects.
    
    Methods:
    --------
    __new__    : Initializes the object and allows a return object
    __str__     : Function that returns an information string of the object.
    """
    
    def __new__(self) -> Union[bool,List[Player]]:
        """
        Function that will ask for the playernames and it will return
        a list of Player objects, if no players then a False is returned.
        
        :returns: a list of Players objects or False if no players.
        """
        
        self.players: List[Player] = []
        plyer=0
        while True:
            plyer+=1
            new_player=input(f"Player {plyer} enter your name please(Return to finish!): ")
            if new_player == '' and plyer == 1:
                return False
            elif new_player == '':
                break #Finished input of players
            self.players.append(Player(new_player))
        return(self.players)


