# https://sudokusolver.app/
# export, include the string into the constructor

#from array import *
#import classes.BoardGenerator as BoardGenerator
from functions import *


# Get Columns
# Get Boxes

# Is board valid

# Get number of answers
board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'

solutions = getNumberOfEmpties(board)
rows=getRows(board)
#print(rows)

columns=getColumns(board)
#print(columns)

boxes=getBoxes(board)
print(boxes)

print('Number of solutions:', solutions**9)

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
