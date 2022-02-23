# Project : challenge-card-game-becode
# FILE: player.py
#
# Author: Bouazzaoui M.
# Date: 23/02/2022
# Version: 1.0
#

from random import choice as rndchoice
from random import shuffle as rndshuffle
from card import Card
from typing import Union, List


class Player:
    """
    The class creates a Player object that holds all the necessary information
    about a player needed to play the game.
    
    Inherited Classes
    -----------------
    none
    
    Attributes
    ----------
    playername:         str 
    cards:              List of Card objects
    turn_count:         int 
    number_of_cards:    int 
    history:            List of Card objects
 
    
    Methods:
    --------
    __init__    : Initializes the object.
    __str__     : Function that returns an information string of the object.
    play        : Selects randomly one of its cards and returns it as a Card object.
                  Prints status information
                  The played card is then removed.
    """

    def __init__(self, playername: str) -> None:
        """
        Init function that will initialize a Player.
        
        :param playername: string 
        """
        self.playername: str = playername
        self.cards: List[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: List[Card] = []

    def play(self) -> Union[Card, None]:
        """
        Function that randomly selects one of its cards. 
        An info status is printed about the players game.
        The played card is removed.
        if no cards are available None is returned else the picked card is
        returned.
         
        :return:        returns the picked object Card or None.
        """

        if self.cards == []:
            return None
        self.turn_count += 1
        card_picked = rndchoice(self.cards)
        self.history.append(card_picked)
        print(
            f"{self.playername} {self.turn_count} played: {card_picked.value} {card_picked.icon}"
        )
        self.cards.remove(card_picked)
        return card_picked

    def __str__(self) -> str:
        """
        Function that creates an information string of the object.
        
        :return: information string.
        """

        info = f"Name:{self.playername} \ncards:{self.cards} \nturn_count:{self.turn_count} \nnumber_of_cards:{self.number_of_cards} \nhistory:{self.history}\n"
        return info


class Deck:
    """
    The class creates a Deck object that holds an empty deck, it allows
    to fill the deck with 52 cards, to shuffle cards and to distribute the
    cards evenly over all the players.
    
    Inherited Classes
    -----------------
    none
    
    Attributes
    ---------- 
    cards:              List of Card objects

    Methods:
    --------
    __init__    : Initializes the object.
    __str__     : Function that returns an information string of the object. 
    fill_deck   : Function that fills the list self.cards with 52 Card objects.   
    shuffle     : Function that shuffles the list self.cards.
    distribute  : Function that distributes evenly to all players.  
    """

    def __init__(self) -> None:
        """
        Init function that will initialize an empty Deck.
        """

        self.cards: [Card] = []  # a list of instances of `Card`

    # fill `cards` with a complete set
    def fill_deck(self) -> None:
        """
        Function that fills the list self.cards with 52 Card objects.
        """
        for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            for icon in ["♥", "♦", "♣", "♠"]:
                self.cards.append(Card(value, icon))

    # shuffle all the list of `cards`
    def shuffle(self) -> None:
        """
        Function that shuffles the list self.cards.
        """
        rndshuffle(self.cards)

    def distribute(self, deck_players: List[Player]) -> None:
        """
        Function that distributes evenly to all players.
        :param deck_players:    a list of Player object
        """

        number_of_players = len(deck_players)
        nxt_card = 0

        for i in self.cards:

            if (52 - nxt_card) < number_of_players:
                break

            for deck_player in deck_players:
                deck_player.cards.append(self.cards[nxt_card])
                nxt_card += 1
                if nxt_card == 52:
                    break

    def __str__(self) -> str:
        """
        Function that creates an information string of the object.
        
        :return: information string.
        """
        info = ""
        for crd in self.cards[::]:
            info = info + str(crd) + ","
        return f"The deck contains following cards: \n{info}"
