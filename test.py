import unittest
from functions import *

class TestFunctions(unittest.TestCase):

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

