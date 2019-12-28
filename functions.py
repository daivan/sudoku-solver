def getNumberOfEmpties(boardAsString):
    counter = 0
    for c in boardAsString:
        if c=='0':
            counter+=1
    return int(counter)

def getRows(boardAsString):
    rows = []
    rowsGenerator=[]
    counter = 0
    for c in boardAsString:
        rowsGenerator.append(int(c))
        counter+=1
        if(counter == 9):
            rows.append(rowsGenerator)
            rowsGenerator=[]
            counter=0
    return rows

def getColumns(boardAsString):

    columns = []
        
    for n in range(0,9):
        columnGenerator=[]
        columnGenerator.append(int(boardAsString[n+0]))
        columnGenerator.append(int(boardAsString[n+9]))
        columnGenerator.append(int(boardAsString[n+18]))
        columnGenerator.append(int(boardAsString[n+27]))
        columnGenerator.append(int(boardAsString[n+36]))
        columnGenerator.append(int(boardAsString[n+45]))
        columnGenerator.append(int(boardAsString[n+54]))
        columnGenerator.append(int(boardAsString[n+63]))
        columnGenerator.append(int(boardAsString[n+72]))
        columns.append(columnGenerator)
    return columns

def getBoxes(boardAsString):
    
    boxes = []
        
    for n in [0,3,6,27,30,33,54,57,60]:
        boxesGenerator=[]
        boxesGenerator.append(int(boardAsString[n+0]))
        boxesGenerator.append(int(boardAsString[n+1]))
        boxesGenerator.append(int(boardAsString[n+2]))
        boxesGenerator.append(int(boardAsString[n+9]))
        boxesGenerator.append(int(boardAsString[n+10]))
        boxesGenerator.append(int(boardAsString[n+11]))
        boxesGenerator.append(int(boardAsString[n+18]))
        boxesGenerator.append(int(boardAsString[n+19]))
        boxesGenerator.append(int(boardAsString[n+20]))
        boxes.append(boxesGenerator)
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
    for n in range (0, 9):
        if index == 0+n or index == 9+n or index == 18+n or index == 27+n or index == 36+n or index == 45+n or index == 54+n or index == 63+n or index == 72+n:
            return n
    return 0

def getBoxByIndex(index):
    for box_id,n in enumerate([0,3,6,27,30,33,54,57,60]):
        if index == n+0 or index == n+1 or index == n+2 or index == n+9 or index == n+10 or index == n+11 or index == n+18 or index == n+19 or index == n+20:
            return box_id

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
    
    output = board[:index] + str(value) + board[index+1:]
    return output

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
        if n=='0' and getBoxByIndex(index)==id:
            boxes.append(index)

    return boxes

def getAllEmptyFromRowId(board, id):
    rows=[]
    for index,n in enumerate(board):
        if n=='0' and getRowByIndex(index)==id:
            rows.append(index)

    return rows

def getAllEmptyFromColumnId(board, id):
    columns=[]
    for index,n in enumerate(board):
        if n=='0' and getColumnByIndex(index)==id:
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
        
        if value == '0':
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
    
    for index, number in enumerate(board):
        if number != '0':
            # check if number already exists in box
            boxes=getBoxes(board)
            box_values=boxes[getBoxByIndex(index)]
            if box_values.count(int(number))>1:
                return False

            # check if number already exists in row
            rows=getRows(board)
            row_values=rows[getRowByIndex(index)]
            if row_values.count(int(number))>1:
                return False

            # check if number already exists in column
            columns=getColumns(board)
            column_values=columns[getColumnByIndex(index)]
            if column_values.count(int(number))>1:
                return False                
    return True

def isBoardComplete(board):

    if isBoardPossible(board) and getNumberOfEmpties(board) == 0:
        return True
    return False

def findEmpty(board):
    for index,n in enumerate(board):
        if n == '0':
            return index

    return None
