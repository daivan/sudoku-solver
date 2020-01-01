from functions import *

def solve(board):

    if isBoardComplete(board):
        print(getBoardAsString(board))
        return True

    # Find the first/next 0    
    find = findEmpty(board)           
    # Find its current options
    options = getOptionsByIndex(board, find)
    
    # Preload all the boxes and the rows and the columns for this solve-state
    boxes=getBoxes(board)
    rows=getRows(board)
    columns=getColumns(board)

    # Loop the options
    for i in options:
        if i in boxes[getBoxByIndex(find)] or i in rows[getRowByIndex(find)] or i in columns[getColumnByIndex(find)]:
            pass
        # Set the current option in the found 0
        setNewValueInBoard(board, find, i)
        # Check if its solved
        if solve(board):
            return True

    # Make sure to set the current 0 to 0 again if it has been trying to be set as something then backtrack
    setNewValueInBoard(board, find, 0)
    return False
        
        
   