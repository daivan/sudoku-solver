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