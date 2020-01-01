from functions import *

def solve(board):

    if isBoardComplete(board):
        print(board)
        return True
    else:
        find = findEmpty(board)       

    options = getOptionsByIndex(board, find)
    for i in options:
        tempBoard = setNewValueInBoard(board, find, i)
        if(isBoardPossible(tempBoard)):
            board = tempBoard
            if solve(board):
                return True

            setNewValueInBoard(board, find, 0)
        
   