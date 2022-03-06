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
                output += str(self.cellsList[row*self.dimension + col].value)
                if((col+1)%3==0): output += " "
            output += "\n\n" if ((row+1)%3==0) else "\n"
        return output
    
    def getCell(self, row, col):
        return self.cellsList[row*self.dimension + col].value
    
    def setCell(self, row, col, val):
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
            
            while(self.getCell(row, col) != 0):
                row = random.randrange(9)
                col = random.randrange(9)
                
            value = None
            # Random definition of the specific cell
            # So we have to verify that the specific number can be assign to that specific cell
            valueList = [1,2,3,4,5,6,7,8,9]
            value = random.randrange(len(valueList))
            while (self.checkBox(row, col, valueList[value]) or self.checkRow(row, valueList[value]) or self.checkCol(col, valueList[value])):
                valueList.remove(valueList[value])
                value = random.randrange(len(valueList))
            cell = Cell(valueList[value])
            self.setCell(row, col, cell)
            
      
    def checkBox(self, row, col, value):
        for r in range(int(row/3)*3, int(row/3)*3+3):
            for c in range(int(col/3)*3, int(col/3)*3+3):
                if (self.getCell(r,c) == value): return True
        return False
        #print("Celle uguali box ",r, c, self.getCell(r,c), value)
    
    def checkRow(self, row, value):
        return any(self.getCell(row, c) == value for c in range(self.dimension))
    #print("Celle uguali riga ",row, c, self.getCell(row,c), value)
    

    def checkCol(self, col, value):
        return any(self.getCell(r, col) == value for r in range(self.dimension))
    #print("Celle uguali ciolonna ",r, col, self.getCell(r,col), value)
    
    
    
    #questo funziona