def getNumberOfEmpties(boardAsString):
    counter = 0
    for c in boardAsString:
        if c==0:
            counter+=1
    return counter

def getRows(boardAsString):
    rows = []
    for n in [0,9,18,27,36,45,54,63,72]:
        rows.append([boardAsString[n+0],boardAsString[n+1],boardAsString[n+2],boardAsString[n+3],boardAsString[n+4],boardAsString[n+5],boardAsString[n+6],boardAsString[n+7],boardAsString[n+8]])
    return rows

def getColumns(boardAsString):

    columns = []
    for n in range(0,9):
        columns.append([boardAsString[n+0],boardAsString[n+9],boardAsString[n+18],boardAsString[n+27],boardAsString[n+36],boardAsString[n+45],boardAsString[n+54],boardAsString[n+63],boardAsString[n+72]])
    return columns

def getBoxes(boardAsString):
    
    boxes = []
    for n in [0,3,6,27,30,33,54,57,60]:
        boxes.append([boardAsString[n+0],boardAsString[n+1],boardAsString[n+2],boardAsString[n+9],boardAsString[n+10],boardAsString[n+11],boardAsString[n+18],boardAsString[n+19],boardAsString[n+20]])
    return boxes

def getBoardAsList(boardAsString):
    board = []
    for c in boardAsString:
        board.append(int(c))
    return board

def getRowByIndex(index):
    if 0 <= index <= 8:
        return 0
    elif 9 <= index <= 17:
        return 1
    elif 18 <= index <= 26:
        return 2
    elif 27 <= index <= 35:
        return 3
    elif 36 <= index <= 44:
        return 4
    elif 45 <= index <= 53:
        return 5
    elif 54 <= index <= 62:
        return 6
    elif 63 <= index <= 71:
        return 7
    elif 72 <= index <= 80:
        return 8

def getColumnByIndex(index):
    if index in [0,9,18,27,36,45,54,63,72]:
        return 0
    elif index in [1,10,19,28,37,46,55,64,73]:
        return 1
    elif index in [2,11,20,29,38,47,56,65,74]:
        return 2            
    elif index in [3,12,21,30,39,48,57,66,75]:
        return 3
    elif index in [4,13,22,31,40,49,58,67,76]:
        return 4
    elif index in [5,14,23,32,41,50,59,68,77]:
        return 5
    elif index in [6,15,24,33,42,51,60,69,78]:
        return 6
    elif index in [7,16,25,34,43,52,61,70,79]:
        return 7
    elif index in [8,17,26,35,44,53,62,71,80]:
        return 8 

def getBoxByIndex(index):
    #for box_id,n in enumerate([0,3,6,27,30,33,54,57,60]):
    #    if index == n+0 or index == n+1 or index == n+2 or index == n+9 or index == n+10 or index == n+11 or index == n+18 or index == n+19 or index == n+20:
    #        return box_id
    if index in [0,1,2,9,10,11,18,19,20]:
        return 0
    elif index in [3,4,5,12,13,14,21,22,23]:
        return 1
    elif index in [6,7,8,15,16,17,24,25,26]:
        return 2
    elif index in [27,28,29,36,37,38,45,46,47]:
        return 3
    elif index in [30,31,32,39,40,41,48,49,50]:
        return 4
    elif index in [33,34,35,42,43,44,51,52,53]:
        return 5
    elif index in [54,55,56,63,64,65,72,73,74]:
        return 6
    elif index in [57,58,59,66,67,68,75,76,77]:
        return 7
    elif index in [60,61,62,69,70,71,78,79,80]:    
        return 8
    

def mergeRowColumnBoxToList(row,column,box):
    first_list = row
    second_list = column
    third_list = box

    #in_first = set(first_list)
    #in_second = set(second_list)
    #in_third = set(third_list)

    merged = [*row , *column , *box]
    merged.sort()
    return listToUnique(merged)
    #result = first_list + list(in_second_but_not_in_first)
    #return result  # Prints [1, 2, 2, 5, 9, 7]
    #pass

def listToUnique(listWithDuplicates):
    return list(set(listWithDuplicates))
    first_list = row
    second_list = column
    third_list = box

    #in_first = set(first_list)
    #in_second = set(second_list)
    #in_third = set(third_list)

    merged = [*row , *column , *box]
    merged.sort()
    return merged
    #result = first_list + list(in_second_but_not_in_first)
    #return result  # Prints [1, 2, 2, 5, 9, 7]
    #pass

def reverseOptionsOnList(reversableList):

    output = []
    for n in range(1,10):
        if not n in reversableList:
            output.append(n)
    return output

def getOptionsByIndex(board, index):
    rows = getRows(board)
    columns = getColumns(board)
    boxes = getBoxes(board)
    row = rows[getRowByIndex(index)]
    column = columns[getColumnByIndex(index)]
    box = boxes[getBoxByIndex(index)]
    value=mergeRowColumnBoxToList(row,column,box)
    options=reverseOptionsOnList(value)
    return options

def setNewValueInBoard(board, index, value):
    
    #output = board[:index] + str(value) + board[index+1:]
    board[index] = value
    return board

def singlePossibilityRule(board):
    if getNumberOfEmpties(board)==0:
        return board

    rows=getRows(board)

    columns=getColumns(board)

    boxes=getBoxes(board)

    boardAsList = getBoardAsList(board)

    BetterBoard = board

    for index,value in enumerate(boardAsList):
        if value==0:
            r=rows[getRowByIndex(index)]
            c=columns[getColumnByIndex(index)]
            b=boxes[getBoxByIndex(index)]
            options = reverseOptionsOnList(mergeRowColumnBoxToList(r,c,b))
        
            if len(options)==1:
                BetterBoard=setNewValueInBoard(BetterBoard, index, options[0])
    
    return BetterBoard

# Run until singlePossibilityRule cant find anymore
def fullSinglePossibilityRule(board):

    while board!=singlePossibilityRule(board):
        board=singlePossibilityRule(board)
    
    return board

def getAllEmptyFromBoxId(board, id):
    boxes=[]
    for index,n in enumerate(board):
        if n==0 and getBoxByIndex(index)==id:
            boxes.append(index)

    return boxes

def getAllEmptyFromRowId(board, id):
    rows=[]
    for index,n in enumerate(board):
        if n==0 and getRowByIndex(index)==id:
            rows.append(index)

    return rows

def getAllEmptyFromColumnId(board, id):
    columns=[]
    for index,n in enumerate(board):
        if n==0 and getColumnByIndex(index)==id:
            columns.append(index)

    return columns


def checkForHiddenSingleByIndex(board, index, listOfIndexes):

    
    possibilities = getOptionsByIndex(board,index)
    allOptions = []
    for listIndex in listOfIndexes:
        options=getOptionsByIndex(board,listIndex)
        allOptions.extend(options)

    numbers = []
    duplicates = []
    uniques = []
    for n in allOptions:
        if n in numbers:
            duplicates.append(n)
        else:
            numbers.append(n)
        
    for n in numbers:
        if not n in duplicates and n in possibilities:
            return n
    
    return False

def hiddenSingle(board):
    if getNumberOfEmpties(board)==0:
        return board


    BetterBoard = board

    for index,value in enumerate(BetterBoard):
        
        if value == 0:
            listOfIndexes = getAllEmptyFromBoxId(board,getBoxByIndex(index))
            newValue = checkForHiddenSingleByIndex(BetterBoard,index,listOfIndexes)
            if(newValue!=False):

                BetterBoard=setNewValueInBoard(BetterBoard, index, newValue)
                continue


            listOfIndexes = getAllEmptyFromRowId(board,getRowByIndex(index))
            newValue = checkForHiddenSingleByIndex(BetterBoard,index,listOfIndexes)
            if(newValue!=False):
                
                BetterBoard=setNewValueInBoard(BetterBoard, index, newValue)
                continue


            listOfIndexes = getAllEmptyFromColumnId(board,getColumnByIndex(index))
            newValue = checkForHiddenSingleByIndex(BetterBoard,index,listOfIndexes)
            if(newValue!=False):
                
                BetterBoard=setNewValueInBoard(BetterBoard, index, newValue)
                continue

    return BetterBoard

def fullHiddenSingle(board):
    
    while board!=hiddenSingle(board):
        board=hiddenSingle(board)
    
    return board

def isBoardPossible(board):
    
    boxes=getBoxes(board)
    rows=getRows(board)
    columns=getColumns(board)

    for index, number in enumerate(board):
        if number != 0:
            # check if number already exists in box
            box_values=boxes[getBoxByIndex(index)]
            if box_values.count(number)>1:
                return False

            # check if number already exists in row
            row_values=rows[getRowByIndex(index)]
            if row_values.count(number)>1:
                return False

            # check if number already exists in column
            column_values=columns[getColumnByIndex(index)]
            if column_values.count(number)>1:
                return False                
    return True

def isBoardComplete(board):

    if 0 not in board and isBoardPossible(board):
        return True
    return False

def findEmpty(board):
    for index,n in enumerate(board):
        if n == 0:
            return index

    return None
