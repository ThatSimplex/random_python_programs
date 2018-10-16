import time
from board import Board

def main():
    board = Board(40, 80)

    choice = input()

    while choice != 'q':
        board.update() 
        time.sleep(0.1)

main()
