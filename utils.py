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
                
def readFile(filename):
    board = []
    with open(filename) as f:
        text = f.readlines()
        board = [list(map(int, x.strip())) for x in text]
    return board
