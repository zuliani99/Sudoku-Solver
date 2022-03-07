from board import SudokuBoard
import sys
from techniques.constraint_propagation import ConstraintPropagation
if __name__ == "__main__":
    board = SudokuBoard(9, sys.argv[1])
    board.createRandomBoard()
    while(not board.fillRandomBoard()):
        board.createRandomBoard()
    print(board)
    cp = ConstraintPropagation(board)
    cp.solve()