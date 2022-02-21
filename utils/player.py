
from card.py import Card
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
        card_picked=random.choice(self.cards)
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
                self.cards.append(Card(value,icon))
        
    #shuffle all the list of `cards`
    def shuffle(self):
        shuffle(self.cards)
        
    #distribute the cards evenly between all the players.
    def distribute(self,players):
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
        
        


        
        
        
        
        
        
        
        
        