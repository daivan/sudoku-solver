# https://sudokusolver.app/
# export, include the string into the constructor

from array import *
from textwrap import wrap
#import classes.BoardGenerator as BoardGenerator
import classes.BoardGenerator as BoardGenerator


class SudokuSolver:

    rows = []
    columns = []
    boxes = []

    def __init__(self, boardAsString):
        self.boardAsString = boardAsString


    def generateBoardFromString(self):
        #self.board=[[2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
        #self.board[0][0]=10
        #print(self.board[0][0])
        #row = 0
        #for c in self.boardAsString:
        #    print(c)
        #print(self.board)
        line = self.boardAsString    
        rows = wrap(line, 9)
        for c in rows:
            print(wrap(c, 1))
        print(columns[0])
        #self.board = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

    def generateGroupsFromString(self):
        s = self.boardAsString
        self.rows.append([s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8]])
        self.rows.append([s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16],s[17]])
        self.rows.append([s[18],s[19],s[20],s[21],s[22],s[23],s[24],s[25],s[26]])
        self.rows.append([s[27],s[28],s[29],s[30],s[31],s[32],s[33],s[34],s[35]])
        self.rows.append([s[36],s[37],s[38],s[39],s[40],s[41],s[42],s[43],s[44]])
        self.rows.append([s[45],s[46],s[47],s[48],s[49],s[50],s[51],s[52],s[53]])
        self.rows.append([s[54],s[55],s[56],s[57],s[58],s[59],s[60],s[61],s[62]])
        self.rows.append([s[63],s[64],s[65],s[66],s[67],s[68],s[69],s[70],s[71]])
        self.rows.append([s[72],s[73],s[74],s[75],s[76],s[77],s[78],s[79],s[80]])

        self.columns = []
        self.columns.append([s[0],s[9],s[18],s[27],s[36],s[45],s[54],s[63],s[72]])
        self.columns.append([s[1],s[10],s[19],s[28],s[37],s[46],s[55],s[64],s[73]])
        self.columns.append([s[2],s[11],s[20],s[29],s[38],s[47],s[56],s[65],s[74]])
        self.columns.append([s[3],s[12],s[21],s[30],s[39],s[48],s[57],s[66],s[75]])
        self.columns.append([s[4],s[13],s[22],s[31],s[40],s[49],s[58],s[67],s[76]])
        self.columns.append([s[5],s[14],s[23],s[32],s[41],s[50],s[59],s[68],s[77]])
        self.columns.append([s[6],s[15],s[24],s[33],s[42],s[51],s[60],s[69],s[78]])
        self.columns.append([s[7],s[16],s[25],s[34],s[43],s[52],s[61],s[70],s[79]])
        self.columns.append([s[8],s[17],s[26],s[35],s[44],s[53],s[62],s[71],s[80]])

        self.boxes = []
        self.boxes.append([s[0],s[1],s[2],s[9],s[10],s[11],s[18],s[19],s[20]])
        self.boxes.append([s[3],s[4],s[5],s[12],s[13],s[14],s[21],s[22],s[23]])
        self.boxes.append([s[6],s[7],s[8],s[15],s[16],s[17],s[24],s[25],s[26]])
        self.boxes.append([s[27],s[28],s[29],s[36],s[37],s[38],s[45],s[46],s[47]])
        self.boxes.append([s[30],s[31],s[32],s[39],s[40],s[41],s[48],s[49],s[50]])
        self.boxes.append([s[33],s[34],s[35],s[42],s[43],s[44],s[51],s[52],s[53]])
        self.boxes.append([s[54],s[55],s[56],s[63],s[64],s[65],s[72],s[73],s[74]])
        self.boxes.append([s[57],s[58],s[59],s[66],s[67],s[68],s[75],s[76],s[77]])
        self.boxes.append([s[60],s[61],s[62],s[69],s[70],s[71],s[78],s[79],s[80]])


    def belongsToRow(self, n):
        if(n==0 or n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8):
            return 0
        elif(n==9 or n==10 or n==11 or n==12 or n==13 or n==14 or n==15 or n==16 or n==17):
            return 1
        elif(n==18 or n==19 or n==20 or n==21 or n==22 or n==23 or n==24 or n==25 or n==26):
            return 2
        elif(n==27 or n==28 or n==29 or n==30 or n==31 or n==32 or n==33 or n==34 or n==35):
            return 3
        elif(n==36 or n==37 or n==38 or n==39 or n==40 or n==41 or n==42 or n==43 or n==44):
            return 4
        elif(n==45 or n==46 or n==47 or n==48 or n==49 or n==50 or n==51 or n==52 or n==53):
            return 5
        elif(n==54 or n==55 or n==56 or n==57 or n==58 or n==59 or n==60 or n==61 or n==62):
            return 6
        elif(n==63 or n==64 or n==65 or n==66 or n==67 or n==68 or n==69 or n==70 or n==71):
            return 7
        elif(n==72 or n==73 or n==74 or n==75 or n==76 or n==77 or n==78 or n==79 or n==80):
            return 8

    def belongsToColumn(self, n):
        if(n==0 or n==9 or n==18 or n==27 or n==36 or n==45 or n==54 or n==63 or n==72):
            return 0
        elif(n==1 or n==10 or n==19 or n==28 or n==37 or n==46 or n==55 or n==64 or n==73):
            return 1
        elif(n==2 or n==11 or n==20 or n==29 or n==38 or n==47 or n==56 or n==65 or n==74):
            return 2
        elif(n==3 or n==12 or n==21 or n==30 or n==39 or n==48 or n==57 or n==66 or n==75):
            return 3
        elif(n==4 or n==13 or n==22 or n==31 or n==40 or n==49 or n==58 or n==67 or n==76):
            return 4
        elif(n==5 or n==14 or n==23 or n==32 or n==41 or n==50 or n==59 or n==68 or n==77):
            return 5
        elif(n==6 or n==15 or n==24 or n==33 or n==42 or n==51 or n==60 or n==69 or n==78):
            return 6
        elif(n==7 or n==16 or n==25 or n==34 or n==43 or n==52 or n==61 or n==70 or n==79):
            return 7
        elif(n==8 or n==17 or n==26 or n==35 or n==44 or n==53 or n==62 or n==71 or n==80):
            return 8

    def belongsToBox(self, n):
        if(n==0 or n==1 or n==2 or n==9 or n==10 or n==11 or n==18 or n==19 or n==20):
            return 0
        elif(n==3 or n==4 or n==5 or n==12 or n==13 or n==14 or n==21 or n==22 or n==23):
            return 1
        elif(n==6 or n==7 or n==8 or n==15 or n==16 or n==17 or n==24 or n==25 or n==26):
            return 2
        elif(n==27 or n==28 or n==29 or n==36 or n==37 or n==38 or n==45 or n==46 or n==47):
            return 3
        elif(n==30 or n==31 or n==32 or n==39 or n==40 or n==41 or n==48 or n==49 or n==50):
            return 4
        elif(n==33 or n==34 or n==35 or n==42 or n==43 or n==44 or n==51 or n==52 or n==53):
            return 5
        elif(n==54 or n==55 or n==56 or n==63 or n==64 or n==65 or n==72 or n==73 or n==74):
            return 6
        elif(n==57 or n==58 or n==59 or n==66 or n==67 or n==68 or n==75 or n==76 or n==77):
            return 7
        elif(n==60 or n==61 or n==62 or n==69 or n==70 or n==71 or n==78 or n==79 or n==80):
            return 8


    def compareRowColumnBox(self, row, column, box):
        print(row,column,box)
        print(self.rows[row])
        print(self.columns[column])
        print(self.boxes[box])

    def isThisFrameOkay(self,index):
        row = self.belongsToRow(index)
        column = self.belongsToColumn(index)
        box = self.belongsToBox(index)
        self.compareRowColumnBox(row, column, box)

    def isBoardComplete(self):
        for index,number in enumerate(self.boardAsString):
            if(self.isThisFrameOkay(index) == False):
                return False
        return True

    def drawBoard(self):
        print('-----BOARD-----')
        #print(self.board)

    def run(self):
        empties = BoardGenerator.GenerateEmpties(self.boardAsString)
        print('Empties',empties)
        constants = BoardGenerator.GenerateConstants(self.boardAsString)
        print('Constants',constants)
        newKey = BoardGenerator.GenerateNewKey(empties)
        print('Key',newKey)

        board = BoardGenerator.applyKeyToConstants(newKey,constants)
        print(newKey,constants, board)
        BoardGenerator.isBoardValid(board)


        # Get Empties
        # Get Constants

        # Generate New Key from Empties
        # Apply Key to Constants
        # Check if board is valid
        # If valid HORAY its been solved
        # Else go back go Generate ...


        #well = 'hejsan'
        #print(well)
        #self.generateGroupsFromString()
        #if(self.isBoardComplete()):
        #    print('You did it!')

        #self.generateGroupsFromString()
        #self.drawBoard()
    

solution = SudokuSolver("920000670061800042045020309050060000600948000094030006000510000200087050080402037")
solution.run()

