import numpy as np

def print_board(mat):
    for i in range(len(mat)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(mat[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(mat[i][j]))
            else:
                print(str(mat[i][j]) + " ", end="")
                
                
def readFile(filename): # retrun numpy array 9x9
    board = np.zeros([9, 9], dtype=int)
    with open(filename) as f:
        for row, line in enumerate(f):
            for col, i in enumerate(line.split(" ")):
                board[row][col] = i
            
    return board