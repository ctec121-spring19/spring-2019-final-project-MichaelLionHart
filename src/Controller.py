# Controller.py
#
# For TicTacToe

from View import *
from Model import *

class Controller:

    def __init__(self):
        self.v = View()
        self.m = Model()

    def play(self):
        done = False
        while not done:
            self.playAGame()
            
            self.v.entry()
            if self.v.entry() is True:
                done = False
            else:
                done = True


    # outer loop that just says play a game and do you want to play another
    def playAGame(self):
        self.v.grid()
        done = False
        personA_turn = True
        self.v.message("Player A's Turn")
        while not done:
            click = self.v.getClickPoint()
            cell = self.v.convertToCell(click)
            # determine if cell is already in gameBoard (True if not)
            if self.m.returnGameBoard(cell) is True:
                if personA_turn is True:
                    self.m.populateBoard(cell, 'X')
                else:
                    self.m.populateBoard(cell, 'O')
            else:
                self.v.message("please choose a valid cell")
            # is there a winner?
            if self.m.winner() is True:
                done = True
                self.v.message("Player A wins!")
            else:
                done = True
                self.v.message("It is a draw")
            personA_turn = False
            self.v.message("Player B's Turn")

    # inner loop gets mouse click - cell number from view, then validates it by calling
    # the model.  It's valid if the cell is empty.  If it's valid/empty, it tells model
    # to put an X or O in the cell

    # ask model if there is a winner or a draw, if not, switch players and continue
    # if there is a winner or a draw, put up approprate message and exit the inner loop method

    # outer loop asks players if they want to play again or not
        pass

def ControllerTest():
    # delete and enter your code here
    pass

if __name__ == "__main__":
    ControllerTest()
