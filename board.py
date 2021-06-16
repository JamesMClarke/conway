from grid_gui import Grid_gui
from square import Square
from tkinter import *
from random import getrandbits
from time import sleep

def main():
    board = Board()
    board.print_new()
    sleep(2)
    board.show_grid()
    board.update_board()
   
    
class Board:
    width = 10
    length = 10

    def __init__(self):
        #Creates a random grid
        self.grid = [[Square(bool(getrandbits(1))) for j in range(self.length)] for i in range(self.width)]
        self.gui =  Grid_gui(self.grid,self.width,self.length)

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
                    print(" ", end ="|")
            print("")
            print("-".join(["-"] * self.width))

    
    def no_of_neighbours(self, x, y):
        neighbours = 0
        
        #Checks if the square above is alive
        if(x-1 >= 0):
            if(self.grid[x-1][y].get_is_alive()):
                neighbours += 1

        #Checks if the square below if alive
        if(x+1 < self.width):
            if(self.grid[x+1][y].get_is_alive()):
                neighbours += 1

        #Checks if the square to the left is alive
        if(y-1 >= 0):
            if(self.grid[x][y-1].get_is_alive()):
                neighbours += 1

        #Checks if the square to the right is alive
        if(y+1 < self.length):
            if(self.grid[x][y+1].get_is_alive()):
                neighbours += 1

        return neighbours

    def tick(self):
        for y in range(0 , self.length):
            for x in range(0, self.width):
                neighbours = self.no_of_neighbours(x ,y)
                print(neighbours, end ="|")
                if(neighbours == 3):
                    self.grid[x][y].revive()
                elif(neighbours != 2):
                    self.grid[x][y].kill()

    
    def grid_gui(self):
        #ToDo put  in a frame
        #ToDo allow user to change state of cell
        #ToDo add user configurable sizing and colouring of rectangles
        #creates tkinter gui grid on a canvas



        #adjust value to change rect size
        rect_size = 15
        
   
    def show_grid(self):
        self.gui.create_grid()

    def update_board(self):
        self.gui.update_gui()

           
                

   
if __name__ == "__main__":
    main()
