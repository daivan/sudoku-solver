# https://sudokusolver.app/
# export, include the string into the constructor

#from array import *
#import classes.BoardGenerator as BoardGenerator
from functions import *



# Very Easy
#board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
# Easy
#board = '200000000070502938008000000320000000700050400004200013002407089009020604400901052'
# Medium
board = '030600040940075000600038092050000000800006070000000438380024000004000320070009084'
#newBoard = singlePossibilityRule(board)
isBoardPossible(board)
newBoard = fullSinglePossibilityRule(board)
newBoard = fullHiddenSingle(newBoard)

cleanBoard = newBoard

# start with clean board
# Get the pointer
# Index
# Options
# Check if board still works
    # Move forward
# Else
    # Try new on the same
    # If no more
    # Go back
    # If no more, update pointer

for index,n in enumerate(newBoard):
    if n == '0':
        options = getOptionsByIndex(newBoard, index)
        print(index, options)
        sum = sum * len(options)

print('solutions: ',sum)