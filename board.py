class SudokuBoard:
    def __init__(self, filename):
        self.dimension = 9
        self.freeCell = '0'
        self.readFile(filename)
    
    def readFile(self, filename):
        with open(filename) as f:
            text = f.readlines()
            self.cellsList = [list(x.strip()) for x in text]
    
    def __str__(self): #ok
        output = ""
        for row in self.cellsList:
            for x in row:
                output += f'{str(x)} '
            output += "\n"
        return output