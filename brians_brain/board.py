import pickle
from cell import Cell
from random import randint

class Board:
    def __init__(self, rows, columns, load):
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for column in range(0, columns)] for row in range(0, rows)]

        for row in range(0, rows):
            for column in range(0, columns):
                self.findNeighbour(column, row)

        if not load:
            self.generate()

    def update(self):
        turnOn = []
        dying = []
        turnOff = []

        for row in range(0, self._rows):
            for column in range(0, self._columns):
                cell = self._grid[row][column]

                aliveNeighbours = cell.aliveNeighbours()

                if cell.isAlive():
                    dying.append(cell)
                elif aliveNeighbours == 2 and cell._status == 'off':
                    turnOn.append(cell)
                elif cell._status == 'dying':
                    turnOff.append(cell)
        
        for cell in turnOn:
            cell.changeStatus()
        
        for cell in turnOff:
            cell.changeStatus()

        for cell in dying:
            cell.changeStatus()
        
        self.drawBoard()

    def drawBoard(self):
        print('\n'*80)

        for row in range(0, self._rows):
            for column in range(0, self._columns):
                cell = self._grid[row][column]
                print(cell.getSymbol(), end='')
            
            print()
    
    def generate(self):
        for row in range(0, self._rows):
            for column in range(0, self._columns):
                seed = randint(0, 3)
                cell = self._grid[row][column]
                
                if seed == 0:
                    cell.changeStatus()

    def findOn(self):
        numDying = 0

        for row in range(0, self._rows):
            for column in range(0, self._columns):
                cell = self._grid[row][column]

                if cell._status == 'dying':
                    numDying += 1

        return numDying

    def findNeighbour(self, x, y):
        cell = self._grid[y][x]
        
        if x == 0 and y == 0:
            cell._neighbours.append(self._grid[y][x+1])
            cell._neighbours.append(self._grid[y+1][x+1])
            cell._neighbours.append(self._grid[y+1][x])
        elif x == 0 and y == self._rows-1:
            cell._neighbours.append(self._grid[y-1][x])
            cell._neighbours.append(self._grid[y-1][x+1])
            cell._neighbours.append(self._grid[y][x+1])
        elif x == self._columns-1 and y == self._rows-1:
            cell._neighbours.append(self._grid[y][x-1])
            cell._neighbours.append(self._grid[y-11][x-11])
            cell._neighbours.append(self._grid[y-11][x])
        elif x == self._columns-1 and y == 0:
            cell._neighbours.append(self._grid[y][x-1])
            cell._neighbours.append(self._grid[y+1][x-1])
            cell._neighbours.append(self._grid[y+1][x])
        elif x < self._columns-1 and y == 0:
            cell._neighbours.append(self._grid[y][x-1])
            cell._neighbours.append(self._grid[y+1][x-1])
            cell._neighbours.append(self._grid[y+1][x])
            cell._neighbours.append(self._grid[y+1][x+1])
            cell._neighbours.append(self._grid[y][x+1])
        elif x < self._columns-1 and y == self._rows-1:
            cell._neighbours.append(self._grid[y][x-1])
            cell._neighbours.append(self._grid[y-1][x-1])
            cell._neighbours.append(self._grid[y-1][x])
            cell._neighbours.append(self._grid[y-1][x+1])
            cell._neighbours.append(self._grid[y][x+1])
        elif x == 0 and y < self._rows-1:
            cell._neighbours.append(self._grid[y-1][x])
            cell._neighbours.append(self._grid[y-1][x+1])
            cell._neighbours.append(self._grid[y][x+1])
            cell._neighbours.append(self._grid[y+1][x+1])
            cell._neighbours.append(self._grid[y+1][x])
        elif x == self._columns-1 and y < self._rows-1:
            cell._neighbours.append(self._grid[y+1][x])
            cell._neighbours.append(self._grid[y+1][x-1])
            cell._neighbours.append(self._grid[y][x-1])
            cell._neighbours.append(self._grid[y-1][x-1])
            cell._neighbours.append(self._grid[y-1][x])
        else:
            cell._neighbours.append(self._grid[y-1][x])
            cell._neighbours.append(self._grid[y-1][x+1])
            cell._neighbours.append(self._grid[y][x+1])
            cell._neighbours.append(self._grid[y+1][x+1])
            cell._neighbours.append(self._grid[y+1][x])
            cell._neighbours.append(self._grid[y+1][x-1])
            cell._neighbours.append(self._grid[y][x-1])
            cell._neighbours.append(self._grid[y-1][x-1])

    def saveGrid(self, filename):
        file = open(filename, 'wb')

        pickle.dump(self._grid, file)
        file.close()

    def loadGrid(self, filename):
        with open(filename, 'rb') as f:
            grid = pickle.load(f)
        
        rows = len(grid)
        columns = len(grid[0])

        self._grid = grid
        self._rows = rows
        self._columns = columns
