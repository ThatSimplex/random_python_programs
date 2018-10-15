class Cell:
    def __init__(self):
        self._status = 'dead'
        self._neighbours = []
    
    def changeStatus(self):
        if self._status == 'dead':
            self._status = 'alive'
        else:
            self._status = 'dead'
    
    def isAlive(self):
        if self._status == 'dead':
            return False
        else:
            return True
    
    def getSymbol(self):
        if self.isAlive():
            return '0'
        else:
            return '.'
    
    def aliveNeighbours(self):
        numAlive = 0

        for neighbour in self._neighbours:
            if neighbour.isAlive():
                numAlive += 1
        
        return numAlive
