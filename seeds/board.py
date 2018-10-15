from cell import Cell
from random import randint

class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for column in range(0, columns)] for row in range(0, rows)]

        for row in range(0, rows):
            for column in range(0, columns):
                self.findNeighbour(column, row)

        self.generate()
        self.drawBoard()

    def update(self):
        born = []
        die = []

        for row in range(0, self._rows):
            for column in range(0, self._columns):
                cell = self._grid[row][column]

                aliveNeighbours = cell.aliveNeighbours()

                if aliveNeighbours == 2 and not cell.isAlive():
                    born.append(cell)
                elif cell.isAlive():
                    die.append(cell)
        
        for cell in born:
            cell.changeStatus()
        
        for cell in die:
            cell.changeStatus()
        
        self.drawBoard()

    def drawBoard(self):
        print('\n'*50)

        for row in range(0, self._rows):
            for column in range(0, self._columns):
                cell = self._grid[row][column]
                print(cell.getSymbol(), end='')
            
            print()
    
    def generate(self):
        for row in range(0, self._rows):
            for column in range(0, self._columns):
                seed = randint(0, 9)
                cell = self._grid[row][column]
                
                if seed == 0:
                    cell.changeStatus()

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