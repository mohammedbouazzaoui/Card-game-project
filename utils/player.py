#Project : challenge-card-game-becode
#FILE: player.py
#
# contains : Class Player, Class Deck 
#

from card import Card
from random import choice as rndchoice
from random import shuffle as rndshuffle

from typing import List
        
class Player:
    """
    A class used to ....
    
    Inherited Classes
    -----------------
    Inherits from ....
    
    Attributes
    ----------
    playername:         str 
    cards:              List[Card] 
    turn_count:         int 
    number_of_cards:    int 
    history:            List[Card]   
 
    
    Methods:
    --------
    play(self) -> Card:  returns a Card
    
    
    
    Raises:
    -------
    Exception is raised for unknown card value.
    """
    def __init__(self,playername: str):
        self.playername: str = playername
        self.cards: List[Card] = [] 
        self.turn_count: int = 0
        self.number_of_cards: int = 0 
        self.history: List[Card] = [] 

    def play(self) -> Card:
        """
        Description:
        ------------
        selects randomly one of its cards and returns it as a Card object.
        print(f'{self.playername} {self.turn_count} played: {card_picked.value} {card_picked.icon}')
        A played card is then removed.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        an object of Card
        """
        
        if self.cards == []:
            return []
        self.turn_count+=1
        card_picked=rndchoice(self.cards)
        self.history.append(card_picked)
        print(f'{self.playername} {self.turn_count} played: {card_picked.value} {card_picked.icon}')
        self.cards.remove(card_picked)
        return card_picked
        
class Deck:
    """
    Description:
    ------------
    selects randomly one of its cards and returns it as a Card object.
    print(f'{self.playername} {self.turn_count} played: {card_picked.value} {card_picked.icon}')
    A played card is then removed.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    an object of Card
    """
    def __init__(self):
        self.cards: [Card] = [] #a list of instances of `Card`
    
    #fill `cards` with a complete card game
    def fill_deck(self) -> None:
        for value in ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            for icon in ['♥', '♦', '♣', '♠']:
                self.cards.append(Card(value,icon))
        
    #shuffle all the list of `cards`
    def shuffle(self) -> None:
        rndshuffle(self.cards)
        
    
    def distribute(self,deck_players: [Player]) -> None:
 
        number_of_players=len(deck_players)
        nxt_card=0
       
        for i in self.cards:
        
            if ((52 - nxt_card) < number_of_players):
                break
            
            for deck_player in deck_players:
                deck_player.cards.append(self.cards[nxt_card])
                nxt_card+=1
                if nxt_card == 52:
                    break


        
        
        
        
        
        
        
        
        