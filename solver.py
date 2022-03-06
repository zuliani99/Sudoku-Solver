from board import SudokuBoard
import sys

if __name__ == "__main__":
    board = SudokuBoard(9, sys.argv[1])
    board.createRandomBoard()
    board.fillRandomBoard()
    print(board)
    print(board.printDomain())