import copy

class ConstraintPropagation:

    def __init__(self, board): #ok
        self.cellsDomain = []
        self.board = board
        self.dimension = 9 #ok
        self.emptyDomainValue = self.dimension + 1 #ok
        self.expandedCells = 0
        self.backwordsCells = 0
        self.fixedCellValue = None #ok
        self.freeCell = 0 #ok
        self.setCellsDomain()
        
        
    def getDomainLength(self, list): #ok
        return self.emptyDomainValue if not list or self.fixedCellValue in list else len(list)

    def getDomain(self, row, col): #ok
        domain = [int(i) for i in range(1, self.dimension + 1)]
        self.domainRow(row, domain)
        self.domainCol(col, domain)
        self.domainBox(row, col, domain)
        return domain
    
    def domainRow(self, row, domain): #ok
        for c in range(self.dimension):
            if self.board[row][c] != self.freeCell:
                if self.board[row][c] in domain:
                    domain.remove(self.board[row][c])
        
    def domainCol(self, col, domain): #ok
        for row in range(self.dimension):
            if self.board[row][col] != self.freeCell:
                if self.board[row][col] in domain:
                    domain.remove(self.board[row][col])

    def domainBox(self, row, col, domain): #ok
        for r in range(int(row/3)*3, int(row/3)*3+3):
            for c in range(int(col/3)*3, int(col/3)*3+3):
                if self.board[r][c] in domain:
                    domain.remove(self.board[r][c])

    def setCellsDomain(self): #ok
        newDomain = []
        
        for row in range(self.dimension):
            for col in range(self.dimension):
                if self.board[row][col] != self.freeCell: newDomain.append([self.fixedCellValue])
                else: newDomain.append(self.getDomain(row,col))
        
        self.cellsDomain = newDomain


    def getNextMRVxy(self): #ok
        cellsDomainMap = list(map(self.getDomainLength, self.cellsDomain))
        minimum = min(cellsDomainMap)
        if minimum == self.emptyDomainValue: return -1
        index = cellsDomainMap.index(minimum)
        return(index // self.dimension, index % self.dimension)    
    

    def isEmptyDomainProduced(self, row, col):
        cellLocation = row * self.dimension + col
        cell = self.cellsDomain.pop(cellLocation)
        if [] in self.cellsDomain:
            self.cellsDomain.insert(cellLocation, cell)
            return True
        else:
            self.cellsDomain.insert(cellLocation, cell)
            return False


    def solve(self):
        location = self.getNextMRVxy()
        if type(location) is not tuple: return (self.board, True, self.expandedCells, self.backwordsCells)

        self.expandedCells += 1
        row, col = location

        for value in self.cellsDomain[row * self.dimension + col]:
            currentState = copy.deepcopy(self.cellsDomain)
            self.board[row][col] = value
            
            self.setCellsDomain()
            if self.isEmptyDomainProduced(row, col):
                self.board[row][col] = self.freeCell
                self.cellsDomain = currentState
                self.backwordsCells += 1
            elif self.solve()[1]: 
                return (self.board, True, self.expandedCells, self.backwordsCells)
            
        return (self.board, False, self.expandedCells, self.backwordsCells)