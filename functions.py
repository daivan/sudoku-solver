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