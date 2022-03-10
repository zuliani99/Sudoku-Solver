import copy
from utils import print_board

def getDomainCells(bo): #ok
        newDomain = []
        
        for row in range(len(bo[0])):
            for col in range(len(bo[0])):
                if bo[row][col] != 0: newDomain.append([None])
                else: newDomain.append(getDomain(row,col, bo))
        
        return newDomain
    
def getDomain(row, col, board): #ok
        domain = [int(i) for i in range(1, 9 + 1)]
        domainRow(row, domain, board)
        domainCol(col, domain, board)
        domainBox(row, col, domain, board)
        return domain
    
def domainRow(row, domain, board): #ok
        for c in range(9):
                if board[row][c] in domain:
                    domain.remove(board[row][c])
        
def domainCol(col, domain, board): #ok
        for row in range(9):
                if board[row][col] in domain:
                    domain.remove(board[row][col])

def domainBox(row, col, domain, board): #ok
        for r in range(int(row/3)*3, int(row/3)*3+3):
            for c in range(int(col/3)*3, int(col/3)*3+3):
                    if board[r][c] in domain:
                        domain.remove(board[r][c])
                
def getLenghtDomain(domain):
    if domain == [] or None in domain: return 10 
    else: return len(domain)
    
def getNextMinimumDomain(domain):
    listMapDomain = list(map(getLenghtDomain, domain))
    minimumFirstList = min(listMapDomain)
    if minimumFirstList == 10: return None
    index = listMapDomain.index(minimumFirstList)
    return(int(index / 9), index % 9)
    
def checkValidAssign(bo, row, col, val):
    bo[row][col] = val
    return [] not in getDomainCells(bo)
    
    
def solve(bo, exp, back):
    domain = getDomainCells(bo)    
    location = getNextMinimumDomain(domain)
    
    if(location is None): return (True, bo, exp, back)
    
    row, col = location
    exp += 1
    for val in domain[row * 9 + col]:
        #print(val, row, col)
        if checkValidAssign(copy.deepcopy(bo), row, col, val):
            bo[row][col] = val
            #print("\n")
            #print_board(bo)
            #print("\n")
            #print("assegnato ", val, row, col)
            print("inner" ,exp, back)
            if(solve(bo, exp, back)[0]):
                #print("finito")
                #print_board(bo)
                return (True, bo, exp, back)
        print("alt")
        back += 1
        print("outer" ,exp, back)
        bo[row][col] = 0
    return (False, bo, exp, back)
    























'''def solving(board):
    print("\n_____________________")
    print_board(board)
    print(solve(board))
    print("\n")
    print_board(board)
    print("\n_____________________")'''
    
    
    
    #get next minimum value
    #if(location is None): return True
    #row, col = location
    #print(row, col)
    #print(domain[row * 9 + col])


'''for i in domain[row * 9 + col]:
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False
    for val in domain[row * 9 + col]:

        if not emptyDomain(row, col, val, copy.deepcopy(bo)):
            bo[row][col] = val
            if(solve(copy.deepcopy(bo))):
                return True
        bo[row][col] = 0

    return False'''