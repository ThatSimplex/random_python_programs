import time
from board import Board

def main():
    board = Board(44, 150)

    choice = input()

    while choice != 'q':
        board.update()     
        numDying = board.findOn()

        if numDying == 0:
            break

        time.sleep(0.1)

main()
