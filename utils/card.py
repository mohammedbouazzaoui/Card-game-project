import random

class Symbol:
    #color=''
    #icon=''
    def __init__(self):
        self.color=random.choice(['red','black'])
        self.icon=random.choice(['♥', '♦', '♣', '♠'])

class Card(Symbol):
    def __init__(self):
        self.value=random.choice(['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K'])
        
        
