# https://sudokusolver.app/
# export, include the string into the constructor

#from array import *
#import classes.BoardGenerator as BoardGenerator
from functions import *
from solver import *

#testBoard = '090000000000000000000000000000000000000000000000000000000000000000000000000000000'

# Very Easy
#testBoard = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
# Easy
#testBoard = '200000000070502938008000000320000000700050400004200013002407089009020604400901052'
# Medium
testBoard = '030600040940075000600038092050000000800006070000000438380024000004000320070009084'
#newBoard = singlePossibilityRule(board)

#isBoardPossible(board)
testBoard = fullSinglePossibilityRule(testBoard)
testBoard = fullHiddenSingle(testBoard)

#cleanBoard = newBoard

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

#allOptions=[]
#pointer = 0
#action = 'Init'


solve(testBoard)

#while pointer < 0:
#while pointer<80:

#    if board[pointer]!='0':
#        print('skipping')
#        pointer += 1
#        continue

#    print(board[pointer])
#    options = getOptionsByIndex(board, pointer)
#    print(options)
#    pointer += 1
    #if(board[pointer]!='0'):
    #    pointer += 1
    #    continue
    #else:
    #    print(pointer)
    #    options = getOptionsByIndex(board, pointer)
    #    for n in options:
    #        print(options)
    #        board = setNewValueInBoard(board, pointer, n)
    #        print(board)
    #        if isBoardComplete(board):
    #            print(board)
    #            break
    #        if isBoardPossible(board):
    #            pointer += 1
    #        else:
    #            print('crap')
        

#for index,n in enumerate(testBoard):
#        options = getOptionsByIndex(newBoard, index)
#        if n=='0':
#            allOptions.append(options)
#        else:
#            allOptions.append([])

#print(allOptions)
#allOptions[0].append(1)
#print(allOptions)
#tryThisCombination(cleanBoard,allOptions)

