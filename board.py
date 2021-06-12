from square import Square
import random
from tkinter import *
import time
from grid_gui import create_grid

def main():
    board = Board()
    board.tick()
    print()
    board.print_new()
    board.show_gui()

class Board:
    width = 3
    length = 8

    def __init__(self):
        #Creates a random grid
        self.grid = [[Square(bool(random.getrandbits(1))) for j in range(self.length)] for i in range(self.width)]
        
        #Creates blank grid for testing
        #elf.grid = [[Square(False) for j in range(self.length)] for i in range(self.width)]

        #Puts an alive square for testing
        #self.grid[0][1].revive()
        #self.grid[2][6].revive()
        #self.grid[1][0].revive()
        #self.grid[1][7].revive()
    
   
    def print_new(self):
        for y in range(0 , self.length):
            for x in range(0, self.width):
                if(self.grid[x][y].get_is_alive()):
                    print("X", end ="|")
                else:
                    print("D", end ="|")
            print("")
            print("-".join(["-"] * self.width))
    
    def no_of_neighbours(self, x, y):
        neighbours = 0
        
        #Checks if the square above is alive
        if(self.grid[x-1][y].get_is_alive()):
            neighbours += 1

        #Checks if the square below if alive
        if(x+1 < self.width):
            if(self.grid[x+1][y].get_is_alive()):
                neighbours += 1

        #Checks if the square to the left is alive
        if(self.grid[x][y-1].get_is_alive()):
            neighbours += 1

        #Checks if the square to the right is alive
        if(y+1 < self.length):
            if(self.grid[x][y+1].get_is_alive()):
                neighbours += 1

        print(neighbours)

        return neighbours

    def tick(self):
        for y in range(0 , self.length):
            for x in range(0, self.width):
                neighbours = self.no_of_neighbours(x ,y)

                if(neighbours == 3):
                    self.grid[x][y].revive()
                elif(neighbours != 2):
                    self.grid[x][y].kill()
    
   
                
                

    def show_gui(self):
        create_grid(self.grid,self.width,self.length)


if __name__ == "__main__":
    main()
