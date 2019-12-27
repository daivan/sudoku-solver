# https://sudokusolver.app/
# export, include the string into the constructor

#from array import *
#import classes.BoardGenerator as BoardGenerator
from functions import *



# Very Easy
#board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
# Easy
board = '200000000070502938008000000320000000700050400004200013002407089009020604400901052'

#newBoard = singlePossibilityRule(board)

newBoard = fullSinglePossibilityRule(board)
newBoard = fullHiddenSingle(newBoard)

print(newBoard)
for index,n in enumerate(newBoard):
    if n == '0':
        options = getOptionsByIndex(newBoard, index)
        #print(options)
        #print(index, n)

#newBoard = hiddenSingle(board)
#print(newBoard)

#print(newBoard)
# Get Empties

#print('Empties',newKey)

# Get Constants

#print('Constants',constants)

# while True:
    # Generate New Key from newKey
    
    #print('Key',newKey)

    # Apply Key to Constants
    
    #print(newKey,constants, board)

    # Check if board is valid
    
        # If valid HORAY its been solved
        #print('Horay you did it')
        # Else go back go Generate ...
