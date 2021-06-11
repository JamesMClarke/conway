from square import Square
import random

def main():
    board = Board()
    board.grid[0][0].revive()
    board.print_grid()

class Board:
    width = 3
    length = 8

    def __init__(self):
        #bool(random.getrandbits(1))
        self.grid = [[Square(False) for j in range(self.length)] for i in range(self.width)]


    def print_grid(self):
        for x in self.grid:
            for y in x:
                if(y.get_is_alive()):
                    print("X", end ="|")
                else:
                    print(" ", end ="|")
            print("")
            print("-".join(["-"] * self.width))

if __name__ == "__main__":
    main()