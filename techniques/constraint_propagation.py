import copy
from ..utils import DIMENSION, getDomainCells

EMPTYDOMAINVALUE = 10
                
                
def getLenghtDomain(domain, cellValue):
    #return EMPTYDOMAINVALUE if not domain or None in domain else len(domain)
    if(len(domain) == 1 and domain[0] == cellValue):
        return EMPTYDOMAINVALUE
    else:
        return len(domain.remove(cellValue)) if cellValue != 0 else len(domain)


def getListMapDoamin(domain, bo):
    map = []
    for row in range(DIMENSION):
        map.extend(
            getLenghtDomain(domain[row * DIMENSION + col], bo[row][col])
            for col in range(DIMENSION))
    return map

def getNextMinimumDomain(domain, bo):
    #listMapDomain = list(map(getLenghtDomain, domain))
    listMapDomain = getListMapDoamin(domain, bo)
    minimumFirstList = min(listMapDomain)
    if minimumFirstList == EMPTYDOMAINVALUE: return None
    index = listMapDomain.index(minimumFirstList)
    return(int(index / DIMENSION), index % DIMENSION)
    
    
def checkValidAssign(bo, row, col, val):
    bo[row][col] = val
    return [] not in getDomainCells(bo)
    
    
def solveConstraintPropagation(bo, exp, back):
    domain = getDomainCells(bo)    
    location = getNextMinimumDomain(domain, bo)
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