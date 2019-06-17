# Controller.py
#
# For TicTacToe

from View import *
from Model import *

class Controller:

    def __init__(self):
        self.v = View()
        self.m = Model(self.v)

    def play(self):
        done = False
        while not done:
            self.playAGame()
            # ask for input from user to determine whether to keep playing
            # if user clicks, continue
            self.v.setMessage('Click to start a new game')
            x = self.v.click()
            if x is True:
                done = False
            else:
                done = True


    # outer loop that just says play a game and do you want to play another
    def playAGame(self):
        done = False
        personA_turn = True
        self.v.setMessage("Player A's Turn")
        while not done:
            cell = self.v.getClickPoint()
            print('get click point finished: ', cell)
            # determine if cell is already in gameBoard (True if not)
            if self.m.returnGameBoard(cell) is True:
                # if it's player A's turn, print 'X' and populate gameBoard with an 'X'
                if personA_turn is True:
                    self.m.populateBoard(cell, 'X')
                # if not, print 'O' and populate gameBoard with an 'O'
                else:
                    self.m.populateBoard(cell, 'O')
            # if cell is already taken, tell user to pick another cell
            else:
                self.v.setMessage("please choose a valid cell")
            # is there a winner?
            if self.m.winner() is True:
                # if so, print winning message and end game
                print('winner')
                self.v.setMessage("Winner!")
                done = True
            # is board full?
            if self.m.boardFull() is True:
                self.v.setMessage("It is a draw")
                done = True
            # is it player A's turn?
            if personA_turn is True:
                personA_turn = False
                self.v.setMessage("Player B's Turn")
            else:
                personA_turn = True
                self.v.setMessage("Player A's Turn")              

        pass
    

def ControllerTest():
    c = Controller()
    c.play()
    pass

if __name__ == "__main__":
    ControllerTest()