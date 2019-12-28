from functions import *

def findEmpty(board):
    for index,n in enumerate(board):
        if n == '0':
            return index

    return None

def solve(board):

    #print(board)
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
        
   