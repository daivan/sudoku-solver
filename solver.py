from functions import *

def find_empty(board):
    for index,n in enumerate(board):
        if n == '0':
            return index

    return None

def solve(board):

    #find = find_empty(board)
    #if not find:
    #    return True
    #else:
    #    print(find)
    
    print(board)
    if isBoardComplete(board):
        print(board)
        return True
    else:
        find = find_empty(board)
        #print(find)
        

    options = getOptionsByIndex(board, find)
    for i in options:
        tempBoard = setNewValueInBoard(board, find, i)
        if(isBoardPossible(tempBoard)):
            board = tempBoard
            if solve(board):
                return True

            setNewValueInBoard(board, find, 0)
        
    #print(find_empty(board))
    #print(board)
    #print(isBoardPossible(board))
    