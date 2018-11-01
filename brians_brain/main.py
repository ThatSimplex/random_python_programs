import time
import sys
from board import Board

def main():
    rows = 40
    columns = 120

    sys.setrecursionlimit(rows * columns * 5)

    load = input('Do you want to load a board from a file? (y/n) ')

    if load.lower() == 'y':
        board = Board(rows, columns, True)
        filename = input('What is the filename of the file you want to load from? ')
        board.loadGrid(filename)
    else:
        board = Board(rows, columns, False)
        board.drawBoard()
        save = input('Do you want to save this board? (y/n) ')

        if save.lower() == 'y':
            filename = input('What will the filename be? ')
            board.saveGrid(filename)

    choice = input('Please press enter to start')

    while True:
        board.update()     
        numDying = board.findOn()

        if numDying == 0:
            break
        
        time.sleep(0.1)

main()
