import copy

class ConstraintPropagation:

    def __init__(self, board): #ok
        self.cellsDomain = []
        self.board = copy.deepcopy(board)
        self.emptyDomainValue = board.dimension + 1
        self.expandedCells = 0
        self.backwordsCells = 0
        self.fixedCellValue = 'X'
        self.setCellsDomain()
        
    def __str__(self): #ok
        output = ""
        for row in self.board.cellsList:
            for x in row:
                output += f'{str(x)} '
            output += "\n"
        output += "Nodes expanded: {}\n".format(self.expandedCells)
        output += "Nodes backword: {}\n".format(self.backwordsCells)
        return output

    def getDomainLength(self, list): #ok
        return self.emptyDomainValue if not list or self.fixedCellValue in list else len(list)

    def getDomain(self, row, col): #ok
        domain = [str(i) for i in range(1, self.board.dimension + 1)]
        self.domainRow(row, domain)
        self.domainCol(col, domain)
        self.domainBox(row, col, domain)
        return domain
    
    def domainRow(self, row, domain): #ok
        for c in range(self.board.dimension):
            if self.board.cellsList[row][c] != self.board.freeCell:
                if self.board.cellsList[row][c] in domain:
                    domain.remove(self.board.cellsList[row][c])
    
    def domainCol(self, col, domain): #ok
        for row in range(self.board.dimension):
            if self.board.cellsList[row][col] != self.board.freeCell:
                if self.board.cellsList[row][col] in domain:
                    domain.remove(self.board.cellsList[row][col])
    
    def domainBox(self, row, col, domain): #ok
        for r in range(int(row/3)*3, int(row/3)*3+3):
            for c in range(int(col/3)*3, int(col/3)*3+3):
                if self.board.cellsList[r][c] in domain:
                    domain.remove(self.board.cellsList[r][c])

    def setCellsDomain(self): #ok
        remainingValues = []
        
        for row in range(self.board.dimension):
            for col in range(self.board.dimension):
                if self.board.cellsList[row][col] != self.board.freeCell: remainingValues.append(self.fixedCellValue)
                else: remainingValues.append(self.getDomain(row,col))
        
        self.cellsDomain = remainingValues


    def getNextMRVxy(self): #ok
        cellsDomainMap = list(map(self.getDomainLength, self.cellsDomain))
        minimum = min(cellsDomainMap)
        if minimum == self.emptyDomainValue: return -1
        index = cellsDomainMap.index(minimum)
        return(int(index / self.board.dimension), index % self.board.dimension)
    

    def isEmptyDomainProduced(self, row, col):
        cellLocation = row * self.board.dimension + col
        cell = self.cellsDomain.pop(cellLocation)
        if [] in self.cellsDomain:
            self.cellsDomain.insert(cellLocation, cell)
            return True
        else:
            self.cellsDomain.insert(cellLocation, cell)
            return False



    def solve(self): #ok
        location = self.getNextMRVxy()
        if type(location) is not tuple: return True

        self.expandedCells += 1
        row = location[0]
        col = location[1]

        for value in self.cellsDomain[row * self.board.dimension + col]:
            currentState = copy.deepcopy(self.cellsDomain)
            self.board.cellsList[row][col] = str(value)
            
            self.setCellsDomain()
            if self.isEmptyDomainProduced(row, col):
                self.backwordsCells += 1
                self.board.cellsList[row][col] = self.board.freeCell
                self.cellsDomain = currentState
            elif self.solve(): 
                return True
            
        return False