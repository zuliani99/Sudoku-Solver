import copy
DIMENSION = 9
FREECELLVALUE = 0
EMPTYDOMAINVALUE = 10


def getDomainCells(bo):
        newDomain = []
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                if bo[row][col] != FREECELLVALUE: newDomain.append([None])
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
                
                
def getLenghtDomain(domain):
    return EMPTYDOMAINVALUE if not domain or None in domain else len(domain)

    
def getNextMinimumDomain(domain):
    listMapDomain = list(map(getLenghtDomain, domain))
    minimumFirstList = min(listMapDomain)
    if minimumFirstList == EMPTYDOMAINVALUE: return None
    index = listMapDomain.index(minimumFirstList)
    return(int(index / DIMENSION), index % DIMENSION)
    
    
def checkValidAssign(bo, row, col, val):
    bo[row][col] = val
    return [] not in getDomainCells(bo)
    
    
def solveConstraintPropagation(bo, exp, back):
    domain = getDomainCells(bo)    
    location = getNextMinimumDomain(domain)
    if(location is None): return (True, bo, exp, back)
    row, col = location
    for val in domain[row * DIMENSION + col]:
        if checkValidAssign(copy.deepcopy(bo), row, col, val):
            exp += 1
            bo[row][col] = val
            solved, board, expanded, backword = solveConstraintPropagation(bo, exp, back)
            if(solved): return (True, board, exp + expanded, back + backword)
        back += 1
        bo[row][col] = 0
    return (False, bo, exp, back)