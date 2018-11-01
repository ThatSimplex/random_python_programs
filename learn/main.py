import time
from board import Board

def main():
    board = Board(40, 100)
    
    while True:
        board.update()
        time.sleep(0.1)

main()