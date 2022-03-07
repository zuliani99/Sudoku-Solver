import copy

class ConstraintPropagation:

    def __init__(self, board): #ok
        #self.cellsList = []
        #self.dimension = dimension
        #self.freeCell = 0
        self.cellsDomain = []
        self.board = copy.deepcopy(board)
        self.emptyDomainValue = board.dimension + 1
        self.expandedCells = 0
        self.setCellsDomain()
        
    def __str__(self): #ok
        output = ""
        for row in self.board.cellsList:
            for x in row:
                output += f'{str(x)} '
            output += "\n"
        return output

    def getDomainLength(self, list): #ok
        return self.emptyDomainValue if not list else len(list)

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
        for row in range(self.board.dimension):
            for col in range(self.board.dimension):
                if self.board.cellsList[row][col] != self.board.freeCell: 
                    empty = []
                    self.cellsDomain.append(empty)
                else: self.cellsDomain.append(self.getDomain(row,col))


    def getNextMRVxy(self): #ok
        cellsDomainMap = list(map(self.getDomainLength, self.cellsDomain))
        minimum = min(cellsDomainMap)
        if minimum == self.emptyDomainValue: return -1
        index = cellsDomainMap.index(minimum)
        return(int(index / self.board.dimension), index % self.board.dimension)
    

    """
    Checks if a cell value assignment produces an empty domain for another cell in the same row, column, or box
    If it does, then we know that cell assignment is not viable
    """
    def isEmptyDomainProduced(self, row, col):
        # Get location of the given cell in the list
        cellLocation = row * self.board.dimension + col

        # Extract the cell we have just assigned a new value to
        cell = self.cellsDomain.pop(cellLocation)

        # If there is an empty domain present now
        if [] in self.cellsDomain:
            # Reinsert the given cell and return True
            self.cellsDomain.insert(cellLocation, cell)
            return True

        # If no empty domain is produced
        else:
            # Reinsert the given cell and return False
            self.cellsDomain.insert(cellLocation, cell)
            return False



    def solve(self): #ok
        location = self.getNextMRVxy()
        if type(location) is not tuple: 
            print("risolto")
            return True

        self.expandedCells += 1
        row = location[0]
        col = location[1]

        for value in self.cellsDomain[row * self.board.dimension + col]:
            currentState = copy.deepcopy(self.cellsDomain)
            self.board.cellsList[row][col] = value
            self.getDomain(row, col)
            
            if self.isEmptyDomainProduced(row, col):
                self.board.cellsList[row][col] = self.board.freeCell
                self.cellsDomain = currentState
            elif self.solve(): 
                print("risolto")
                return True
            
        return False

    #def printBoard(self): print(self.board)