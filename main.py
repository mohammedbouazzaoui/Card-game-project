#MAIN
######
from game import Inviteplayers,Board

players=Inviteplayers()
if players == False:
    print("No players ? No game !")
else:
    mygame=Board(players)
    mygame.start_game()
