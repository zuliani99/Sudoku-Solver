from board import SudokuBoard
from techniques.constraint_propagation import ConstraintPropagation
from techniques.relaxation_labelling import RelaxationLabelling
from os import listdir
import pandas as pd

resultCP = []
resultRL = []

def solveCP(board, filename):
    cp = ConstraintPropagation(board)
    print(filename)
    print("Initial Sudoku Board:\n" + str(board))
    solved, time, exp, back = cp.solve()
    print("Solved Sudoku Board:\n" + str(cp))
    print(f"Board was solved: {solved} in time {str(time)} with {exp} expanded nodes and {back} backword nodes\n\n")
    resultCP.append([filename, time, exp, back, solved])
    
def solveRL(board, filename):
    rl = RelaxationLabelling(board)
    print(filename)
    print("Initial Sudoku Board:\n" + str(board))
    solved, time, n_iter = rl.solve()
    print("Solved Sudoku Board:\n" + str(rl))
    print(f"Board was solved: {solved} in time {str(time)} with {n_iter} iterations\n\n")
    resultRL.append([filename, n_iter, solved])

if __name__ == "__main__":
    easySudoku = listdir("./examples/easy")
    normalSudoku = listdir("./examples/normal")
    #mediumSudoku = [f for f in listdir("./examples/medium") if isfile(join("./examples/medium", f))]
    #hardSudoku = [f for f in listdir("./examples/hard") if isfile(join("./examples/hard", f))]

    print("EASY SUDOKU")
    for easy in sorted(easySudoku): 
        solveCP(SudokuBoard(f"./examples/easy/{easy}".format()), easy.split(".")[0])
        #solveRL(SudokuBoard(f"./examples/easy/{easy}".format()), easy.split(".")[0])

    print("\nNORMAL SUDOKU")
    for normal in sorted(normalSudoku): 
        solveCP(SudokuBoard(f"./examples/normal/{normal}".format()), normal.split(".")[0])
        #solveRL(SudokuBoard(f"./examples/normal/{normal}".format()), normal.split(".")[0])

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
    
    #print("RESULTS FOR RELAXATION LABELLING")
    #df_resultRL = pd.DataFrame(resultRL, columns=["Filename", "NUmber_of_Iteration", "Solved"])
    #print(df_resultRL.to_string(index=False))
    
    df_resultCP.to_csv("./results/cp_result.csv", index=False)
    #df_resultRL.to_csv("./results/rl_result.csv", index=False)
    