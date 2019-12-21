# https://sudokusolver.app/
# export, include the string into the constructor

from array import *
from textwrap import wrap
#import classes.BoardGenerator as BoardGenerator
import classes.BoardGenerator as BoardGenerator


class SudokuSolver:

    def __init__(self, boardAsString):
       self.boardAsString = boardAsString

    def run(self):

        # Get Empties
        newKey = BoardGenerator.GenerateEmpties(self.boardAsString)
        print('Empties',newKey)

        # Get Constants
        constants = BoardGenerator.GenerateConstants(self.boardAsString)
        print('Constants',constants)

        while True:
            # Generate New Key from newKey
            newKey = BoardGenerator.GenerateNewKey(newKey)
            print('Key',newKey)

            # Apply Key to Constants
            board = BoardGenerator.applyKeyToConstants(newKey,constants)
            print(newKey,constants, board)

            # Check if board is valid
            if(BoardGenerator.isBoardValid(board)):
                # If valid HORAY its been solved
                print('Horay you did it')
                print(board)
                break
                # Else go back go Generate ...

    

solution = SudokuSolver("603200059010400263059030410002160090801504007000809005067002000100307080000040000")
solution.run()

