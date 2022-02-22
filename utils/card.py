#FILE: card.py

class Symbol:
    def __init__(self,icon: chr ):
        self.icon=icon #(['♥', '♦', '♣', '♠'])
        if icon == '♦' or icon == '♥':
            self.color = 'red'
        elif icon == '♣' or icon == '♠':        
            self.color = 'black'  
        else:
            raise Exception("Unknown icon!")
            
class Card(Symbol):
    def __init__(self,value: str,icon: chr):
        super().__init__(icon)
        if value in ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            self.value = value
        else:
            raise Exception("Unknown card value!")
