#README FILE
#############
#Author: Bouazzaoui M.
#Date: 23/02/2022
#

## DESCRIPTION
--------------
The game will simulate players that receive cards from 52 carddeck and
will simulate a game game by having every player pick automatically
a random card and play it against the other players.
So for every round evey player has to show one card.
When all the cards have been shown, the game ends.
This is a game to be run in command mode no graphics available.


## INSTALLATION
---------------
copy following files to the same directory:

main.py
card.py
game.py
player.py


## USAGE
---------

from the same directory you can start the game with:
python main.py

The game will ask for the names of all players. End the input with an empty return.
This will start the game, a carddeck will generated and shuffled. The cards will be
evenly distributed to the players.
The players will pick randomly a card from their cards and play this card.
One round is when every player has shown his card.

The game ends when the players have used all their cards.
You can only follow a play simulation on screen for now.

