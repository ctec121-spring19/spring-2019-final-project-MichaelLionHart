# Model.py
#
# For TicTacToe

from View import *

# container to hold gameboard values (X's and O's)
gameBoard = ['', '', '', '', '', '', '', '', '']

class Model:
    ''' keeps track of what's in each cell (X, O, or empty).  It updates its data when
        the controller calls it with a move.  It also provides the logic.  A method can 
        be called if there is a winner.  This method would examine the cell values to see 
        if there are three in a row.  It would also tell if there is a draw - i.e. no 
        winner but all cells are full. '''

    def __init__(self, view):
        self.v = view

    # function to validate mouse-click/cell number (check if empty)
    def winner(self):
        # horizontal cells
        if gameBoard[0] == gameBoard[1] and gameBoard[0] == gameBoard[2] and gameBoard[0] != '':
            print("True")
            return True
        elif gameBoard[3] == gameBoard[4] and gameBoard[3] == gameBoard[5] and gameBoard[3] != '':
            print("True")
            return True
        elif gameBoard[6] == gameBoard[7] and gameBoard[6] == gameBoard[8] and gameBoard[6] != '':
            print("True")
            return True
        # vertical cells
        elif gameBoard[0] == gameBoard[3] and gameBoard[0] == gameBoard[6] and gameBoard[0] != '':
            print("True")
            return True
        elif gameBoard[1] == gameBoard[4] and gameBoard[1] == gameBoard[7] and gameBoard[1] != '':
            return True
        elif gameBoard[2] == gameBoard[5] and gameBoard[2] == gameBoard[8] and gameBoard[2] != '':
            return True
        # diagonal cells
        elif gameBoard[0] == gameBoard[4] and gameBoard[0] == gameBoard[8] and gameBoard[0] != '':
            return True
        elif gameBoard[2] == gameBoard[4] and gameBoard[2] == gameBoard[6] and gameBoard[2] != '':
            return True

    # function to check if board is full - return True or False to Controller
    def boardFull(self):
        container = []
        for i in gameBoard:
            if i == 'X' or i == 'O':
                container.append('N')
        print('length of container is: ', len(container))
        if len(container) == 9:
            return True

    # function to determine if specified cell is in the gameboard already
    def returnGameBoard(self, cell):
        if cell not in gameBoard:
            return True

    # function to clear the board so game play can resume
    def clearBoard(self):
        gameBoard[0] = ''
        gameBoard[1] = ''
        gameBoard[2] = ''
        gameBoard[3] = ''
        gameBoard[4] = ''
        gameBoard[5] = ''
        gameBoard[6] = ''
        gameBoard[7] = ''
        gameBoard[8] = ''


    # function to put an X or O in the cell, based on controller call, then 
    # call view to draw appropriate symbol
    def populateBoard(self, cell, symbol):
        if cell == 'cell0':
            gameBoard[0] = symbol
            self.v.draw(cell, symbol)
        elif cell == 'cell1':
            gameBoard[1] = symbol
            self.v.draw(cell, symbol)
        elif cell == 'cell2':
            gameBoard[2] = symbol
            self.v.draw(cell, symbol)
        elif cell == 'cell3':
            gameBoard[3] = symbol
            self.v.draw(cell, symbol)
        elif cell == 'cell4':
            gameBoard[4] = symbol
            self.v.draw(cell, symbol)
        elif cell == 'cell5':
            gameBoard[5] = symbol
            self.v.draw(cell, symbol)
        elif cell == 'cell6':
            gameBoard[6] = symbol
            self.v.draw(cell, symbol)
        elif cell == 'cell7':
            gameBoard[7] = symbol
            self.v.draw(cell, symbol)
        elif cell == 'cell8':
            gameBoard[8] = symbol
            self.v.draw(cell, symbol)
        pass

def ModelTest():
    m = Model()
    m.winner()
    # print(m.boardFull())
    pass

if __name__ == "__main__":
    ModelTest()