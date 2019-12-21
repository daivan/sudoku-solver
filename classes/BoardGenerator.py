def GenerateEmpties(string):
    empties = ''
    for c in string: 
        if c == '0': 
            empties+='0'
    return empties

def GenerateConstants(string):
    output=[]
    for c in string: 
        output.append(int(c))
    return output

    return 'Here are your constants'

def GenerateNewKey(oldKey):
    strippedZeros=oldKey.replace("0", "1")
    
    oldKeyAsInt = int(strippedZeros)
    newKeyAsInt=1+oldKeyAsInt
    newKeyAsString=str(newKeyAsInt)
    newKeyStrippedZeros=newKeyAsString.replace("0", "1")

    return newKeyStrippedZeros

def applyKeyToConstants(key,constants):
    board = []
    counter = 0
    for n in constants:
        if(n==0):
            board.append(int(key[counter]))
            counter+=1
        else:
            board.append(n)
    return board

def isBoardValid(board):
    sum = 0
    for n in board:
        sum+=n

    if(sum == 405):
        return True
    else:
        return False