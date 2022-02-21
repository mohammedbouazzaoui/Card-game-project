import random

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
        
