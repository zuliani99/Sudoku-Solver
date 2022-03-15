from techniques.constraint_propagation import solveConstraintPropagation
from techniques.relaxation_labelling import solveRelaxationLabeling
from os import listdir
import pandas as pd
from techniques.utils import checkSolution, readFile, writeFile
from time import time

#https://printablecreative.com/sudoku-generator
#solveSudoku("./examples/easy/easy1.txt".format())

resultCP = []
resultRL = []

easySudoku = listdir("./examples/easy")
normalSudoku = listdir("./examples/normal")
mediumSudoku = listdir("./examples/medium")
hardSudoku = listdir("./examples/hard")


def solveCP(filename):
    board = readFile(filename)
    print(f"Constraint Propagation - Solving: {filename}")
    start = time()
    solved, board, exp, back = solveConstraintPropagation(board, 0, 0)
    end = time()
    #print(solved, checkSolution(board))
    resultCP.append([filename.split("/")[3], str(end - start), exp, back, solved])
    writeFile("cp_solved_boards", filename.split("/")[3], board)
    
    
def solveRL(filename):
    board = readFile(filename)
    print(f"Relaxation Labelling - Solving: {filename}")
    start = time()
    board, n_iter = solveRelaxationLabeling(board)
    end = time()
    resultRL.append([filename, str(end - start), n_iter, checkSolution(board)])
    writeFile("rl_solved_boards", filename.split("/")[3], board)


def solveSudoku(filename):
    solveCP(filename)
    solveRL(filename)


if __name__ == "__main__":

    print("EASY SUDOKU")
    for easy in sorted(easySudoku): solveSudoku(f"./examples/easy/{easy}".format())    

    print("\nNORMAL SUDOKU")
    for normal in sorted(normalSudoku): solveSudoku(f"./examples/normal/{normal}".format())

    print("\nMEDIUM SUDOKU")
    for medium in sorted(mediumSudoku): solveSudoku(f"./examples/medium/{medium}".format())
        
    print("\nHARD SUDOKU")
    for hard in sorted(hardSudoku): solveSudoku(f"./examples/hard/{hard}".format())
       
    print("\n\nRESULTS FOR CONSTRAINT PROPAGATION")
    df_resultCP = pd.DataFrame(resultCP, columns=["Filename", "Execution_Time", "Expanded_Nodes", "Backward_Nodes", "Solved"])
    print(df_resultCP.to_string(index=False))

    print("\n\nRESULTS FOR RELAXATION LABELLING")
    df_resultRL = pd.DataFrame(resultRL, columns=["Filename", "Execution_Time", "Number_of_Iteration", "Solved"])
    print(df_resultRL.to_string(index=False))

    df_resultCP.to_csv("./results/cp_result.csv", index=False)
    df_resultRL.to_csv("./results/rl_result.csv", index=False)