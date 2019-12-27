import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    def test_getNumberOfEmpties(self):
        board = '951386724734259168268174935123765849597438216486912357619843572042597681875621403'
        self.assertEqual(getNumberOfEmpties(board), 2, "getNumberOfEmpties test 1")

        board = '42597681875621443'
        self.assertEqual(getNumberOfEmpties(board), 0, "getNumberOfEmpties test 2")
        
        board = '00000'
        self.assertEqual(getNumberOfEmpties(board), 5, "getNumberOfEmpties test 3")
        
        board = '0110'
        self.assertEqual(getNumberOfEmpties(board), 2, "getNumberOfEmpties test 4")

    def test_getRows(self):
        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        rows=getRows(board)
        self.assertCountEqual(rows[0], [9,0,1,3,0,0,0,0,0], "same array")
        self.assertCountEqual(rows[1], [0,0,0,2,5,0,0,6,8], "same array")
        self.assertCountEqual(rows[8], [0,7,0,0,0,0,4,0,0], "same array")


    def test_getColumns(self):
        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        rows=getColumns(board)
        self.assertCountEqual(rows[0], [9,0,0,0,0,0,6,0,0], "same array")
        self.assertCountEqual(rows[3], [3,2,0,0,0,0,0,5,0], "same array")
        self.assertCountEqual(rows[8], [0,8,0,0,0,7,2,0,0], "same array")

    def test_getBoxes(self):
        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        rows=getBoxes(board)
        self.assertCountEqual(rows[0], [9,0,1,0,0,0,0,6,8], "same array")
        self.assertCountEqual(rows[1], [3,0,0,2,5,0,0,0,4], "same array")
        self.assertCountEqual(rows[2], [0,0,0,0,6,8,0,0,0], "same array")
        self.assertCountEqual(rows[6], [6,1,9,0,4,0,0,7,0], "same array")
        self.assertCountEqual(rows[7], [0,4,3,5,9,7,0,0,0], "same array")
        self.assertCountEqual(rows[8], [0,7,2,0,0,0,4,0,0], "same array")
        

    def test_getBoardAsList(self):
        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        boardAsList=getBoardAsList(board)
        self.assertCountEqual(boardAsList, [9,0,1,3,0,0,0,0,0,0,0,0,2,5,0,0,6,8,0,6,8,0,0,4,0,0,0,0,2,3,0,6,0,0,4,0,0,0,7,0,3,0,0,1,0,0,8,6,0,1,0,0,5,7,6,1,9,0,4,3,0,7,2,0,4,0,5,9,7,0,0,0,0,7,0,0,0,0,4,0,0], "same array")
        
    def test_getRowByIndex(self):
        
        self.assertEqual(getRowByIndex(0), 0, "same row")
        self.assertEqual(getRowByIndex(12), 1, "same row")
        self.assertEqual(getRowByIndex(20), 2, "same row")
        self.assertEqual(getRowByIndex(30), 3, "same row")
        self.assertEqual(getRowByIndex(40), 4, "same row")
        self.assertEqual(getRowByIndex(50), 5, "same row")
        self.assertEqual(getRowByIndex(60), 6, "same row")
        self.assertEqual(getRowByIndex(70), 7, "same row")
        self.assertEqual(getRowByIndex(80), 8, "same row")
        
        
    def test_getColumnByIndex(self):
        
        self.assertEqual(getColumnByIndex(0), 0, "same row")
        self.assertEqual(getColumnByIndex(1), 1, "same row")
        self.assertEqual(getColumnByIndex(2), 2, "same row")
        self.assertEqual(getColumnByIndex(3), 3, "same row")
        self.assertEqual(getColumnByIndex(4), 4, "same row")
        self.assertEqual(getColumnByIndex(5), 5, "same row")
        self.assertEqual(getColumnByIndex(6), 6, "same row")
        self.assertEqual(getColumnByIndex(7), 7, "same row")
        self.assertEqual(getColumnByIndex(8), 8, "same row")
        self.assertEqual(getColumnByIndex(9), 0, "same row")
        self.assertEqual(getColumnByIndex(10), 1, "same row")
        self.assertEqual(getColumnByIndex(11), 2, "same row")
        self.assertEqual(getColumnByIndex(12), 3, "same row")
        self.assertEqual(getColumnByIndex(13), 4, "same row")
        self.assertEqual(getColumnByIndex(14), 5, "same row")
        self.assertEqual(getColumnByIndex(15), 6, "same row")
        self.assertEqual(getColumnByIndex(16), 7, "same row")
        self.assertEqual(getColumnByIndex(17), 8, "same row")
        
    def test_getBoxByIndex(self):
        
        self.assertEqual(getBoxByIndex(0), 0, "same row")
        self.assertEqual(getBoxByIndex(4), 1, "same row")
        self.assertEqual(getBoxByIndex(7), 2, "same row")
        self.assertEqual(getBoxByIndex(27), 3, "same row")
        self.assertEqual(getBoxByIndex(31), 4, "same row")
        self.assertEqual(getBoxByIndex(35), 5, "same row")
        self.assertEqual(getBoxByIndex(73), 6, "same row")
        self.assertEqual(getBoxByIndex(77), 7, "same row")
        self.assertEqual(getBoxByIndex(80), 8, "same row")
        pass

        
    def test_mergeRowColumnBoxToList(self):
        row = [1,2,4,5,6,7,8,9]
        column=[]
        box=[]
        
        self.assertCountEqual(mergeRowColumnBoxToList(row,column,box), [1,2,4,5,6,7,8,9], "same row")

        row = [1,2,2,2,4,5,6,7,8]
        column = [2,3,4,5]
        box = [2,3,4,5]

        self.assertEqual(mergeRowColumnBoxToList(row,column,box), [1,2,3,4,5,6,7,8], "same row")

        pass

    def test_listToUnique(self):
        listWithDuplicates=[1,1,2,2,3,5,6,2,1,1,1,1]
        self.assertEqual(listToUnique(listWithDuplicates), [1,2,3,5,6], "same row")

    def test_reversableList(self):
        reversableList=[1,2,3,5,6]
        self.assertEqual(reverseOptionsOnList(reversableList), [4,7,8,9], "same row")

    def test_setNewValueInBoard(self):
        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        result = '951300000000250068068004000023060040007030010086010057619043072040597000070000400'
        index = 1
        value = 5
        newboard=setNewValueInBoard(board,index,value)
        self.assertEqual(newboard, result, "same row")
        
        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        result = '901380000000250068068004000023060040007030010086010057619043072040597000070000400'
        index = 4
        value = 8
        newboard=setNewValueInBoard(board,index,value)
        self.assertEqual(newboard, result, "same row")

        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        result = '101300000000250068068004000023060040007030010086010057619043072040597000070000400'
        index = 0
        value = 1

        newboard=setNewValueInBoard(board,index,value)
        self.assertEqual(newboard, result, "same row")

        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        result = '901300000000250068068004000023060040007030010086010057619043072040597000070000401'
        index = 80
        value = 1

        newboard=setNewValueInBoard(board,index,value)
        self.assertEqual(newboard, result, "same row")        

    def test_singlePossibilityRule(self):
        board = '901300000000250068068004000023060040007030010086010057619043072040597000070000400'
        
        result = '951300020034250068068074000023060049007030010486010057619843072042597000070000400'
        newboard=singlePossibilityRule(board)
        self.assertEqual(newboard, result, "singlePossibilityRule test 1")  

        result = '951380724734250068268074000023760849597030016486910057619843572042597000075020400'
        newboard=singlePossibilityRule(newboard)
        self.assertEqual(newboard, result, "singlePossibilityRule test 2")
                
        board = '951386724734259168268174935123765849597438216486912357619843572342597681875621493'
        result = '951386724734259168268174935123765849597438216486912357619843572342597681875621493'
        newboard=singlePossibilityRule(board)
        self.assertEqual(newboard, result, "singlePossibilityRule test 3") 

    def test_getOptionsByIndex(self):
        board = '203000700176542938008000200325000897701050426004200513002407189009020674407901352'
        index = 7
        options = getOptionsByIndex(board,index)
        self.assertEqual(options, [4, 6], "getOptionsByIndex test 1") 


    def test_getAllEmptyFromBoxId(self):
        board = '203000700176542938008000200325000897701050426004200513002407189009020674407901352'
        index = 6
        empties = getAllEmptyFromBoxId(board,index)
        self.assertEqual(empties, [54, 55, 63, 64, 73], "getAllEmptyFromBoxId test 1") 

    def test_getAllEmptyFromRowId(self):
        board = '203000700176542938008000200325000897701050426004200513002407189009020674407901352'
        index = 0
        empties = getAllEmptyFromRowId(board,index)
        self.assertEqual(empties, [1, 3, 4, 5, 7, 8], "getAllEmptyFromRowId test 1") 

    def test_getAllEmptyFromColumnId(self):
        board = '203000700176542938008000200325000897701050426004200513002407189009020674407901352'
        index = 0
        empties = getAllEmptyFromColumnId(board,index)
        self.assertEqual(empties, [18, 45, 54, 63], "getAllEmptyFromColumnId test 1") 

    def test_HiddenSingle(self):
        board = '203000700176542938008000200325000897701050426004200513002407189009020674407901352'
        result = '203000700176542938008700200325004897701050426004270513002405189019020674407901352'
        afterSingle = hiddenSingle(board)
        self.assertEqual(afterSingle, result, "HiddenSingle test 1") 



if __name__ == '__main__':
    unittest.main()

#901300000 9
#000250068 18
#068004000 27
#023060040 36
#007030010 45
#086010057 54
#619043072 63
#040597000 72
#070000400 81

