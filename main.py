# Project : challenge-card-game-becode
# FILE: main.py
#
# Author: Bouazzaoui M.
# Date: 23/02/2022
# Version: 1.0
#
"""
Main file :
    invites the players to enter there name and starts the game.
"""
from game import Board, Inviteplayers

print("\n\n\nWelcome in casino WeTakeYourMoney")
print("#################################")
print("Players enter your name, lets play a round of cards !!\n")

players = Inviteplayers()
print("\n\n\nHere we go !!\n\n\n")
if players == False:
    print("No players ? No game !")
else:
    mygame = Board(players)
    mygame.start_game()
