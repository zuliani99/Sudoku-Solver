class Cell:
    def __init__(self, value):
        self.value = value
        self.possibleValue = [1,2,3,4,5,6,7,8,9]
    
    def removeValue(self, value):
        self.possibleValue.remove(value)
    
    def __str__(self):
        return str(self.value)