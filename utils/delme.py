#Project : challenge-card-game-becode
#FILE: card.py
#Author: Bouazzaoui Mohammed
#

class Symbol:
    """
    The class creates a Symbol object with an icon and corresponding color.
    
    Attributes
    ----------
    icon : character string one of these: ['♥', '♦', '♣', '♠']
    color : the color of the icon
    
    Methods:
    --------
    __init__
    __str__
    
    Raises:
    -------
    TypeError : ('Exception: Unknown icon!')
    """
    
    def __init__(self,icon: chr ):
        """
        Init function that will initialize an icon and set its color. If icon is
        unknown then color will be empty.
        
        :param icon: a char string that will be one of ['♥', '♦', '♣', '♠']
        """
        if icon not in ['♥', '♦', '♣', '♠']:
            raise TypeError('Exception: Unknown icon!')
        self.icon=icon 
        if icon == '♦' or icon == '♥':
            self.color = 'red'
        elif icon == '♣' or icon == '♠':        
            self.color = 'black'  
     
    def __str__(self):
        info=str(self.icon) + ' ' + str(self.color)
        return info 
    
class Card(Symbol):
    """
    Class Cards create an object Card with its value and icon.
    
    Inherited Classes
    -----------------
    Inherits from class Symbol
    
    Attributes
    ----------
    value : list of strings of one of these ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    Methods:
    --------
    __init__
    __str__
    
    Raises:
    -------
    TypeError("Exception: Unknown card value!")
    """
    
    def __init__(self,value: str,icon: chr):
        """
        Init function that will initialize a card using the received value and 
        icon.
        
        :param value: a str 
        :param icon: a char string that will be one of ['♥', '♦', '♣', '♠']
        :raises: Exception is raised if value is unknown
        """
        super().__init__(icon)
        if value not in ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            raise TypeError("Exception: Unknown card value!")
        
        self.value = value
        
    def __str__(self):
            info=str(self.value) + ' ' + str(self.icon)
            return info 
        
