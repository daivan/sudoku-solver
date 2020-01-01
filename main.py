# https://sudokusolver.app/
# export, include the string into the constructor

from solver import *
import timeit

# Empty Board
#board = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'
# Very Easy
#board = '700159230305000000000320000001406580040205017507980002400008060050000700080713400'
# Easy
#board = '100036078000050002000270610000300467000160005000090000070049003605002040900583000'
# Medium
#board = '800001609000897050000400810040000786025708900000030000900000170004080002003200008'
# Hard
#board = '600400000020085640007301500006208003830000006005009800090800700000954102000000000'
# Fiendish
board = '000000005009460000703005409500070000100006053206008000060017030071050002000009000'

board = getBoardAsList(board)

start = timeit.default_timer()
for i in range(1,1000):
    isBoardPossible(board)
stop = timeit.default_timer()
print("Time: ", stop - start)

# Try some simple sudoku rules first to clear some easy 0s
#board = fullSinglePossibilityRule(board)
#board = fullHiddenSingle(board)

# Print unsolved board
#print(board)

# Prints Solved board
#start = timeit.default_timer()
#solve(board)
#stop = timeit.default_timer()
        
#print("Time: ", stop - start)