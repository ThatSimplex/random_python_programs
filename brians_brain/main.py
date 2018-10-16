import time
import sys
from board import Board

def main():
    sys.setrecursionlimit(30000)

    load = input('Do you want to load a board from a file? (y/n)')

    if load.lower() == 'y':
        board = Board(30, 60, True)
    
        filename = input('What is the filename of the file you want to load from? ')
        board.loadGrid(filename)
    else:
        board = Board(30, 60, False)

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
