import time
from board import Board

def main():
    board = Board(30, 60)

    choice = input()

    while choice != 'q':
        board.update()
        choice = input()
        # time.sleep(0.1)

main()