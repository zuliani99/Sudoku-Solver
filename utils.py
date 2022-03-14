DIMENSION = 9
FREECELLVALUE = 0

def getDomainCells(bo):
        newDomain = []
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                #if bo[row][col] != FREECELLVALUE: newDomain.append([None]) 
                if bo[row][col] != FREECELLVALUE: newDomain.append([bo[row][col]])
                else: newDomain.append(getDomain(row,col, bo))
        return newDomain
    
    
def getDomain(row, col, board):
        domain = [int(i) for i in range(1, DIMENSION + 1)]
        domainRow(row, domain, board)
        domainCol(col, domain, board)
        domainBox(row, col, domain, board)
        return domain
    
    
def domainRow(row, domain, board):
        for c in range(DIMENSION):
                if board[row][c] in domain:
                    domain.remove(board[row][c])
        
        
def domainCol(col, domain, board):
        for row in range(DIMENSION):
                if board[row][col] in domain:
                    domain.remove(board[row][col])


def domainBox(row, col, domain, board):
        for r in range(int(row/3)*3, int(row/3)*3+3):
            for c in range(int(col/3)*3, int(col/3)*3+3):
                    if board[r][c] in domain:
                        domain.remove(board[r][c])

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

def writeFile(technique, filename, board):
    f = open(f"./results/{technique}/{filename}", "w+")
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == 8:
                f.write(str(board[i][j]) + "\n")
            else:
                f.write(str(board[i][j]))