import copy
import numpy as np

class ConstraintPropagation:

    def __init__(self, board): #ok
        self.cellsDomain = np.empty([9,9])
        self.board = board #np array matrix
        self.dimension = 9 #ok
        self.emptyDomainValue = 10 #ok
        self.expandedCells = 0
        self.backwordsCells = 0
        self.fixedCellValue = 10 #ok
        self.freeCell = 0 #ok
        self.setCellsDomain()
        
        
    def getDomainLength(self, list): 
        print(list)
        return self.emptyDomainValue if not list or self.fixedCellValue in list else len(list)


    def getDomain(self, row, col): #ok
        domain = np.arange(1, 10)
        self.domainRow(row, domain)
        self.domainCol(col, domain)
        self.domainBox(row, col, domain)
        return domain
    
    
    def domainRow(self, row, domain): #ok
        for c in range(self.dimension):
            if self.board[row][c] != self.freeCell:
                print(np.delete(domain, np.where(domain == self.board[row][c])[0]))
                domain = np.delete(domain, np.where(domain == self.board[row][c])[0]) 
        
        
    def domainCol(self, col, domain): #ok
        for r in range(self.dimension):
            if self.board[r][col] != self.freeCell:
                domain = np.delete(domain, np.where(domain == self.board[r][col])[0]) 


    def domainBox(self, row, col, domain): #ok
        for r in range(int(row/3)*3, int(row/3)*3+3):
            for c in range(int(col/3)*3, int(col/3)*3+3):
                domain = np.delete(domain, np.where(domain == self.board[r][c])[0]) 



    def setCellsDomain(self): #ok
        newDomain = []
    
        for row in range(self.dimension):
            for col in range(self.dimension):
                if self.board[row][col] != self.freeCell: newDomain.append([self.fixedCellValue])
                else: newDomain.append(self.getDomain(row,col))
                
        self.cellsDomain = np.reshape(np.asarray(newDomain, dtype=object),(9,9))
        #print(self.cellsDomain)


    def getNextMRVxy(self): #ok
        cellsDomainMap = list(map(self.getDomainLength, (np.reshape(self.cellsDomain, (1,81)).tolist())))
        minimum = min(cellsDomainMap)
        if minimum == self.emptyDomainValue: return -1
        index = cellsDomainMap.index(minimum)
        return(int(index / self.dimension), index % self.dimension)    
    

    def isEmptyDomainProduced(self, row, col):
        listCell = self.cellsDomain.tolist()
        cellLocation = row * self.dimension + col
        cell = listCell.pop(cellLocation)
        if [] in self.cellsDomain:
            listCell.insert(cellLocation, cell)
            self.cellsDomain = np.array(listCell).reshape(9,9)
            return True
        else:
            listCell.insert(cellLocation, cell)
            self.cellsDomain = np.array(listCell).reshape(9,9)
            return False


    def solve(self):
        location = self.getNextMRVxy()
        if type(location) is not tuple: return (self.board, True, self.expandedCells, self.backwordsCells)

        self.expandedCells += 1
        row, col = location

        for value in self.cellsDomain[row][col]:
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