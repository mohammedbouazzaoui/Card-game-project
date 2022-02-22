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
        Function that will initialize the icon and set its color.
        
        :param icon: a char string that will be one of ['♥', '♦', '♣', '♠']
        :raises: raise an exception if icon is unknown.
        """
        self.icon=icon 
        if icon == '♦' or icon == '♥':
            self.color = 'red'
        elif icon == '♣' or icon == '♠':        
            self.color = 'black'  
        else:
            self.color = ''

            
    def __str__(self):
        info=str(self.icon) + ' ' + str(self.color)
        return info 
    
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
        
        Returns
        -------
        None
        
        Raises
        ------
        Exception is raised for unknown card value.
        """
        
        super().__init__(icon)
        if value in ['A', '2', '3','4','5','6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            self.value = value
        else:
            raise Exception("Unknown card value!")


a=Symbol('♥')
print(a.__str__())
print(a)
print(str(a))
print(a.__repr__())
    
class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString
    def __str__ (self):
        return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'
myObject = MyClass(12345, "Hello")

print(myObject.__str__())
print(myObject)
print(str(myObject))
print(myObject.__repr__())