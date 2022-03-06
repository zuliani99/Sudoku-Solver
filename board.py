from cell import Cell
import random

diff = {
    "easy": 32,
    "medium": 30,
    "hard": 28
}

class SudokuBoard:
    def __init__(self, dimension, difficulty):
        self.cellsList = []
        self.dimension = dimension
        self.freeCell = 0
        self.difficulty = diff.get(difficulty)
    
    def __str__(self):
        output = ""
        for row in range(self.dimension):
            for col in range(self.dimension):
                output += str(self.cellsList[row*self.dimension + col].value) + " "
            output += "\n"
        return output
    
    def printDomain(self):
        output = ""
        for row in range(self.dimension):
            for col in range(self.dimension):
                output += str(self.cellsList[row*self.dimension + col].domain) + " "
            output += "\n"
        return output
    
    def getCell(self, row, col) -> Cell:
        return self.cellsList[row*self.dimension + col]
    
    def setCell(self, row, col, val): #val tipo Cell
        self.cellsList[row*self.dimension + col] = val
        #self.cellsList[row*self.dimension + col].possibleValue.remove(val)
    
    def createRandomBoard(self):
        for _ in range(self.dimension):
            for _ in range(self.dimension):
                self.cellsList.append(Cell(self.freeCell))
                
                
    #difficolta media filla 30 celle
    def fillRandomBoard(self):
        for _ in range(self.difficulty):
            
            row = random.randrange(9)
            col = random.randrange(9)
            
            while(self.getCell(row, col).value != 0):
                row = random.randrange(9)
                col = random.randrange(9)
                
            value = None
            # Random definition of the specific cell
            # So we have to verify that the specific number can be assign to that specific cell
            #valueList = [1,2,3,4,5,6,7,8,9]
            cell = self.getCell(row, col) #riferimento
            value = random.randrange(len(cell.domain))
            while (self.checkBox(row, col, cell.domain[value]) or self.checkRow(row, cell.domain[value]) or self.checkCol(col, cell.domain[value])):
                cell.domain.remove(cell.domain[value])
                value = random.randrange(len(cell.domain))
            #cell = Cell(valueList[value])
            #self.setCell(row, col, cell)
            cell.value = value
            
    
    def checkBox(self, row, col, value):
        for r in range(int(row/3)*3, int(row/3)*3+3):
            for c in range(int(col/3)*3, int(col/3)*3+3):
                if (self.getCell(r,c).value == value): return True
        return False
        #print("Celle uguali box ",r, c, self.getCell(r,c), value)
    
    def checkRow(self, row, value):
        return any(self.getCell(row, c).value == value for c in range(self.dimension))
    #print("Celle uguali riga ",row, c, self.getCell(row,c), value)
    

    def checkCol(self, col, value):
        return any(self.getCell(r, col).value == value for r in range(self.dimension))
    #print("Celle uguali ciolonna ",r, col, self.getCell(r,col), value)
    
    
    #def updateDomainCellBox():
    
    #def updateDomainCellRow():
            
    #def updateDomainCellCol():