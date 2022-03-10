#from techniques.constraint_propagation import solve
from constraint_prop2 import solve
from techniques.relaxation_labelling import RelaxationLabelling
from os import listdir
import pandas as pd
from utils import print_board, readFile
from time import time

resultCP = []
resultRL = []

def solveCP(filename):
    board = readFile(filename) 
    print(filename)
    print("Initial Sudoku Board:")
    print_board(board)
    start = time()
    solved, board, exp, back = solve(board, 0, 0)
    end = time()
    print("\nSolved Sudoku Board:")
    print_board(board)
    print(f"\nBoard was solved: {solved} in time {str(end - start)} with {exp} expanded nodes and {back} backword nodes\n\n")
    resultCP.append([filename.split("/")[3], str(end - start), exp, back, solved])
    
def solveRL(board, filename):
    board = readFile(filename) # retrun np.array matrix 9x9
    rl = RelaxationLabelling(board)
    print(filename)
    print("Initial Sudoku Board:")
    print_board(board)
    solved, time, n_iter = rl.solve()
    print("\nSolved Sudoku Board:")
    print_board(board)
    print(f"Board was solved: {solved} in time {str(time)} with {n_iter} iterations\n\n")
    resultRL.append([filename, n_iter, solved])

def solveSudoku(filename):
    solveCP(filename)
    #solveRL(filename)

if __name__ == "__main__":
    easySudoku = listdir("./examples/easy")
    normalSudoku = listdir("./examples/normal")
    #mediumSudoku = [f for f in listdir("./examples/medium") if isfile(join("./examples/medium", f))]
    #hardSudoku = [f for f in listdir("./examples/hard") if isfile(join("./examples/hard", f))]

    print("EASY SUDOKU")
    for easy in sorted(easySudoku): solveSudoku(f"./examples/easy/{easy}".format())
    #solveSudoku("./examples/normal/normal3.txt".format())

    print("\nNORMAL SUDOKU")
    for normal in sorted(normalSudoku): solveSudoku(f"./examples/normal/{normal}".format())

    '''
    for medium in mediumSudoku:
        solveCP(SudokuBoard(f"./examples/medium/{medium}".format()), medium.split(".")[0])
        solveRL(SudokuBoard(f"./examples/medium/{medium}".format()), medium.split(".")[0])
        
    for hard in hardSudoku:
        solveCP(SudokuBoard(f"./examples/hard/{hard}".format()), hard.split(".")[0])
        solveRL(SudokuBoard(f"./examples/hard/{hard}".format())), hard.split(".")[0])
        
    '''

    print("RESULTS FOR CONSTRAINT PROPAGATION")
    df_resultCP = pd.DataFrame(resultCP, columns=["Filename", "Execution_Time", "Expanded_Nodes", "Backward_Nodes", "Solved"])
    print(df_resultCP.to_string(index=False))

    #print("\n\nRESULTS FOR RELAXATION LABELLING")
    #df_resultRL = pd.DataFrame(resultRL, columns=["Filename", "NUmber_of_Iteration", "Solved"])
    #print(df_resultRL.to_string(index=False))

    df_resultCP.to_csv("./results/cp_result.csv", index=False)
    #df_resultRL.to_csv("./results/rl_result.csv", index=False)
    