from square import Square

class Board:
    width = 8
    length = 8

    def __init__(self):
        self.grid = [[Square(False) for j in range(self.width)] for i in range(self.length)]


    def print_grid(self):
        for x in self.grid:
            for y in x:
                if(y.get_is_alive()):
                    print("X", end ="|")
                else:
                    print(" ", end ="|")
            print("")
            print("-".join(["-"] * self.width))

board = Board()
board.print_grid()
