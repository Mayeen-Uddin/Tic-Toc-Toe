"""
File: tictactoegrid.py
Defines the TicTacToeGrid class.
"""

from tictactoesquare import TicTacToeSquare
from turtle import goto, tracer, up, update, write, hideturtle

class TicTacToeGrid(object):
    """Represents a Tic-Tac-Toe grid."""
    def __init__(self, length, xPos, yPos,
                 outlineColor = "black", fillColor = "white",
                 letter = "X"):
        """Sets the initial state of the Tic-Tac-Toe grid."""
        self._letter = letter
        self._grid = list()
        index = 0
        y = yPos
        tracer(False)
        for row in range(3):
            x = xPos
            for column in range(3):
                square = TicTacToeSquare(index, self, length, x, y,
                                       outlineColor, fillColor)
                self._grid.append(square)
                x +=length
                index += 1
            y -= length
            update()
            tracer(True)

    def makeMove(self, index):
        """Respond to a user's click in a square."""
        square = self._grid[index]
        if square.text() == "":
            square.text(self._letter)
            if self._letter == "X":
                self._letter = "O"
            else:
                self._letter = "X"
            winner = self._hasWinner()
            if winner:
                up()
                hideturtle()
                goto(-40, 110)
                write(winner + " wins!", font = ("Arial", 24, "bold"))

    def _hasWinner(self):
        """Returns the letter of the winner or the empty string
        if there is no winner."""
        row0 = self._getString(0, 1, 2)
        row1 = self._getString(3, 4, 5)
        row2 = self._getString(6, 7, 8)
        col0 = self._getString(0, 3, 6)
        col1 = self._getString(1, 4, 7)
        col2 = self._getString(2, 5, 8)
        dia0 = self._getString(0, 4, 8)
        dia1 = self._getString(6, 4, 2)
        if row0 == "OOO" or row1 == "OOO" or row2 == "OOO" or \
           col0 == "OOO" or col2 == "OOO" or col2 == "OOO" or \
           dia0 == "OOO" or dia1 == "OOO":
            return "O"
        elif row0 == "XXX" or row1 == "XXX" or row2 == "XXX" or \
             col0 == "XXX" or col2 == "XXX" or col2 == "XXX" or \
             dia0 == "XXX" or dia1 == "XXX":
            return "X"
        else:
            return ""

    def _getString(self, one, two, three):
        """Build and returns a string from a row, column,
        diagonal of the grid."""
        return self._grid[one].text() + self._grid[two].text() + \
               self._grid[three].text()
