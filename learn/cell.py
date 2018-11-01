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
        if self._status == 'alive':
            return True
        else:
            return False
    
    def getSymbol(self):
        if self.isAlive():
            return 'O'
        else:
            return '.'
    
    def aliveNeighbours(self):
        numAlive = 0

        for neighbour in self._neighbours:
            if neighbour.isAlive():
                numAlive += 1
        
        return numAlive