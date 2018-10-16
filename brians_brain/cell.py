class Cell:
    def __init__(self):
        self._status = 'off'
        self._neighbours = []
    
    def changeStatus(self):
        if self._status == 'off':
            self._status = 'on'
        elif self._status == 'on':
            self._status = 'dying'
        else:
            self._status = 'off'
    
    def isAlive(self):
        if self._status == 'on':
            return True
        else:
            return False
    
    def getSymbol(self):
        if self.isAlive():
            return '0'
        elif self._status == 'dying':
            return 'X'
        else:
            return '.'
    
    def aliveNeighbours(self):
        numAlive = 0

        for neighbour in self._neighbours:
            if neighbour.isAlive():
                numAlive += 1
        
        return numAlive
