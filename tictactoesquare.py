"""
File: tictactoesquare.py
Defines the TicTacToeSquare class.
"""

from turtle import Turtle

class TicTacToeSquare(Turtle):
    """Represent a Tic-Tac-Toe Square."""

    FONT = ("Arial", 12, "bold")

    def __init__(self, index, grid, length, xPos, yPos,
                 outlineColor = "black", fillColor = "white", text = ""):
        """Sets the initial state of the Tic-Tac-Toe Square."""
        Turtle.__init__(self, shape = "square", visible = False)
        self.speed(0)
        self.color(outlineColor, fillColor)
        self.up()
        self.goto(xPos, yPos)
        self.resizemode("user")
        self.shapesize( length / 20, length / 20)
        self._text = text
        self._index = index
        self._grid = grid
        self.onclick(lambda x, y: self._grid.makeMove(self._index))
        self.showturtle()

    def text(self, text = None):
        """Getter and setter for text"""
        if not text is None:
            self._text = text
            self.write(text, align = "center", font = TicTacToeSquare.FONT)
        return self._text
