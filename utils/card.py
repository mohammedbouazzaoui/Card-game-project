#Project : challenge-card-game-becode
#FILE: card.py
#

class Symbol:
    """
    A class used to represent the card icons with their appropriate colors.
    
    Attributes
    ----------
    icon : character string one of these: ['♥', '♦', '♣', '♠']
    color : the color of the icon
    
    Methods:
    --------
    None
    
    Raises:
    -------
    Exception is raised for unknown icon
    """
    
    def __init__(self,icon: chr ):
        """
        Parameters
        ----------
        icon : character string one of these ['♥', '♦', '♣', '♠']
        color : string with 'red' for ['♥', '♦'], 'black' for ['♣', '♠']
        
        Raises
        ------
        Exception is raised for unknown icon.
        """
        
        self.icon=icon 
        if icon == '♦' or icon == '♥':
            self.color = 'red'
        elif icon == '♣' or icon == '♠':        
            self.color = 'black'  
        else:
            raise Exception("Unknown icon!")
            
class Card(Symbol):
    """
    A class used to represent a card with its symbols.
    
    Inherited Classes
    -----------------
    Inherits from class Symbol
    
    Attributes
    ----------
    value : list of strings of one of these ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    Methods:
    --------
    None
    
    Raises:
    -------
    Exception is raised for unknown card value.
    """
    def __init__(self,value: str,icon: chr):
        """
        Parameters
        ----------
        value : list of strings of one of these ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']
        icon : character string one of these ['♥', '♦', '♣', '♠']
        
        Raises
        ------
        Exception is raised for unknown card value.
        """
        
        super().__init__(icon)
        if value in ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            self.value = value
        else:
            raise Exception("Unknown card value!")
