"""
File: tictactoeapp.py
A Tic-Tac-Toe application.
"""

from tictactoegrid import TicTacToeGrid
from turtle import bgcolor, hideturtle, mainloop, pencolor, title

def main():
    hideturtle()
    bgcolor("black")
    pencolor("white")
    title("Tic-Tac-Toe")
    TicTacToeGrid(70, -70, 70, "white", "purple")
    return "Done!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
