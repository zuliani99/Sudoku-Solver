from board import SudokuBoard
from techniques.constraint_propagation import ConstraintPropagation
from os import listdir
from time import time

def solveCP(board):
    cp = ConstraintPropagation(board)
    print("Initial Sudoku Board:\n")
    print(board)
    start = time()
    flag = cp.solve()
    end = time()
    print("Solved Sudoku Board:\n")
    print(cp)
    print("Board was solved: ", flag)
    print(f"Time elapsed: {str(end - start)}" + "\n\n")

if __name__ == "__main__":
    easySudoku = listdir("./examples/easy")
    #normalSudoku = listdir("./examples/normal")
    #mediumSudoku = [f for f in listdir("./examples/medium") if isfile(join("./examples/medium", f))]
    #hardSudoku = [f for f in listdir("./examples/hard") if isfile(join("./examples/hard", f))]
    
    print("EASY SUDOKU")
    for easy in easySudoku: solveCP(SudokuBoard(("./examples/easy/" + easy).format()))
        
    #print("\nNORMAL SUDOKU")
    #for normal in normalSudoku: solveCP(SudokuBoard((("./examples/normal/" + normal).format())))
        
    '''for medium in mediumSudoku:
        board = SudokuBoard(medium)
        
    for hard in hardSudoku:
        board = SudokuBoard(hard)'''