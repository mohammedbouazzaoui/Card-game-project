# Project : challenge-card-game-becode
# FILE: main.py
#
# Author: Bouazzaoui M.
# Date: 23/02/2022
# Version: 1.0
#

from game import Board,Inviteplayers

players = Inviteplayers()

if players == False:
    print("No players ? No game !")
else:
    mygame = Board(players)
    mygame.start_game()
