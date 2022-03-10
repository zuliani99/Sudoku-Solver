import copy
DIMENSION = 9
FREECELL = 0
EMPTYDOMAINVALUECELL = 10
FIXEDCELLVALUE = None
            
def getDomainLength(list): #ok
        return EMPTYDOMAINVALUECELL if not list or FIXEDCELLVALUE in list else len(list)

def getDomain(row, col, board): #ok
        domain = [int(i) for i in range(1, DIMENSION + 1)]
        domainRow(row, domain, board)
        domainCol(col, domain, board)
        domainBox(row, col, domain, board)
        return domain
    
def domainRow(row, domain, board): #ok
        for c in range(DIMENSION):
            if board[row][c] != FREECELL:
                if board[row][c] in domain:
                    domain.remove(board[row][c])
        
def domainCol(col, domain, board): #ok
        for row in range(DIMENSION):
            if board[row][col] != FREECELL:
                if board[row][col] in domain:
                    domain.remove(board[row][col])

def domainBox(row, col, domain, board): #ok
        for r in range(int(row/3)*3, int(row/3)*3+3):
            for c in range(int(col/3)*3, int(col/3)*3+3):
                if board[r][c] in domain:
                    domain.remove(board[r][c])

def setCellsDomain(board): #ok
        newDomain = []
        
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                if board[row][col] != FREECELL: newDomain.append([FIXEDCELLVALUE])
                else: newDomain.append(getDomain(row,col, board))
        
        return newDomain

def getNextMRVxy(domain): #ok
        cellsDomainMap = list(map(getDomainLength, domain))
        minimum = min(cellsDomainMap)
        if minimum == EMPTYDOMAINVALUECELL: return None
        index = cellsDomainMap.index(minimum)
        return(int(index / DIMENSION), index % DIMENSION)    
    

def isEmptyDomainProduced(row, col, domain):
        cellLocation = row * DIMENSION + col
        cell = domain.pop(cellLocation)
        flag = [] in domain
        domain.insert(cellLocation, cell)
        return flag

def solving(domain, board, exp, back):
        location = getNextMRVxy(domain)
        #print(location)
        if location is None: return (board, True, exp, back)

        row, col = location
        #if actualDomain is None:
        for val in domain[row * DIMENSION + col]:
            #self.solve(row, col, copy.deepcopy(domain))
            exp += 1

            currentDomain = copy.deepcopy(domain)
            newBoard = copy.deepcopy(board)
            newBoard[row][col] = val
            newDomain = setCellsDomain(newBoard)
            
            if isEmptyDomainProduced(row, col, newDomain):
                print("sonos")
                newBoard[row][col] = FREECELL
                domain = currentDomain
                 
            elif solving(newDomain, newBoard, exp, back + 1)[1]:
                return (board, True, exp, back)
            
            
            #return self.solving(currentDomain, newBoard)
        return (board, False, exp, back) 
    
def solve(board): 
    print("ok")
    return solving(setCellsDomain(board), board, 0, 0)