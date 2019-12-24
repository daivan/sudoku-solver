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
        

if __name__ == '__main__':
    unittest.main()

#901300000
#000250068
#068004000
#023060040
#007030010
#086010057
#619043072
#040597000
#070000400

