from grid_gui import Grid_gui
from square import Square
from tkinter import *
from random import getrandbits
import asyncio


async def main():
  

    gui =  Grid_gui()
    global b_width
    b_width = gui.get_width()
    global b_length
    b_length = gui.get_length()
    #board.print_new()
    print(gui.get_width())
    board = Board()
    gui.create_grid(board.grid,board.width,board.length)
    while True:
        await asyncio.sleep(1)
        board.tick()
        gui.update_gui()
    
class Board:
    

    def __init__(self):
        self.length = b_length
        self.width = b_width
        #Creates a random grid
        self.grid = [[Square(bool(getrandbits(1))) for j in range(self.length)] for i in range(self.width)]
        #Creates blank grid for testing
        #elf.grid = [[Square(False) for j in range(self.length)] for i in range(self.width)]

        #Puts an alive square for testing
        #self.grid[0][1].revive()
        #self.grid[2][6].revive()
        #self.grid[1][0].revive()
        #self.grid[1][7].revive()
        
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
                if(neighbours == 3):
                    self.grid[x][y].revive()
                elif(neighbours != 2):
                    self.grid[x][y].kill()
   
if __name__ == "__main__":
    asyncio.run(main())