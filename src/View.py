# View.py
# 
# For TicTacToe

from graphics import *


class View:

    def __init__(self):
        # Creating graphics window
        self.win = GraphWin("Mike's Tic Tac Toe Game", 600, 600)
        # creating a way to display messages
        self.message = Text(Point(4, 7.5), '')
        # drawing message
        self.message.draw(self.win)
        # creating grid
        self.grid()


    # function for grid
    def grid(self):
        # Grid line creation
        self.win.setCoords(0, 0, 8, 8)

        # Draw main box
        Rectangle(Point(1, 1), Point(7, 7)).draw(self.win)

        # draw vertical lines
        Line(Point(3, 7), Point(3, 1)).draw(self.win)
        Line(Point(5, 7), Point(5, 1)).draw(self.win)

        # draw horizontal lines
        Line(Point(1, 5), Point(7, 5)).draw(self.win)
        Line(Point(1, 3), Point(7, 3)).draw(self.win)        
        
    # function to return coords when clicked
    # return a cell number
    def getClickPoint(self):
        p = self.win.getMouse()
        return self.convertToCell(p)
        #return (p.getX(), p.getY())

    def click(self):
        x = self.win.getMouse()
        if x is True:
            return True

    # function to display the appropriate message
    def setMessage(self, message):
        self.message.setText(message)

    # function to draw X or O
    def draw(self, cell, symbol):
        #p = self.win.getMouse()
        #px = p.getX()
        #py = p.getY()

        # convert cell to coordinate.
        if cell == 'cell0':
            print(cell)
            coordinate = Point(2, 2)
        elif cell == 'cell1':
            print(cell)
            coordinate = Point(4, 2)
        elif cell == 'cell2':
            print(cell)
            coordinate = Point(6, 2)
        elif cell == 'cell3':
            print(cell)
            coordinate = Point(2, 4)
        elif cell == 'cell4':
            print(cell)
            coordinate = Point(4, 4)
        elif cell == 'cell5':
            print(cell)
            coordinate = Point(6, 4)
        elif cell == 'cell6':
            print(cell)
            coordinate = Point(2, 6)
        elif cell == 'cell7':
            print(cell)
            coordinate = Point(4, 6)
        elif cell == 'cell8':
            print(cell)
            coordinate = Point(6, 6)
        else:
            self.setMessage("Please choose a valid cell")

        message = Text(coordinate, symbol)
        message.setSize(36)
        message.draw(self.win)

    # function to convert mouse click to cell number
    def convertToCell(self, click):
        print(click)
        pX = round(click.getX())
        pY = round(click.getY())
        print(pX)
        print(pY)
        
        if 1 <= pX <= 3 and 1 <= pY <= 3:
            return "cell0"
        elif 3 <= pX <= 5 and 1 <= pY <= 3:
            return "cell1"
        elif 5 <= pX <= 7 and 1 <= pY <= 3:
            return "cell2"
        elif 1 <= pX <= 3 and 3 <= pY <= 5:
            return "cell3"
        elif 3 <= pX <= 5 and 3 <= pY <= 5:
            return "cell4"
        elif 5 <= pX <= 7 and 3 <= pY <= 5:
            return "cell5"
        elif 1 <= pX <= 3 and 5 <= pY <= 7:
            return "cell6"
        elif 3 <= pX <= 5 and 5 <= pY <= 7:
            return "cell7"
        elif 5 <= pX <= 7 and 5 <= pY <= 7:
            return "cell8"
        else: 
            return "invalid"

def ViewTest():
    v = View()
    v.setMessage("test")
    # v.getClickPoint()
    # v.drawX()
    # v.drawO()
    # v.message("Player A's Turn")
    # v.convertToCell()

    input()

    
if __name__ == "__main__":
    ViewTest()