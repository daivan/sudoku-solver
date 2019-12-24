def getNumberOfEmpties(boardAsString):
    counter = 0
    for c in boardAsString:
        if c=='0':
            counter+=1
    return int(counter)