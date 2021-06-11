from square import Square
import random

def main():
    board = Board()
    board.grid[2][0].revive()
    board.print_new()

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

    def print_new(self):
        for y in range(0 , self.length):
            for x in range(0, self.width):
                if(self.grid[x][y].get_is_alive()):
                    print("X", end ="|")
                else:
                    print(" ", end ="|")
            print("")
            print("-".join(["-"] * self.width))

if __name__ == "__main__":
    main()