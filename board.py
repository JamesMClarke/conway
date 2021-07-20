from square import Square
from boards import Board_Type
from random import getrandbits
from cords import Cords
    
class Board:
    #TODO Make variables protected
    def __init__(self, width, length, grid, type):
        self.length = length
        self.width = width
        #If the user want's a random board
        if(type == Board_Type['random']):
            #Creates a random grid
            self.grid = [[Square(bool(getrandbits(1))) for j in range(self.length)] for i in range(self.width)]
        #Otherwise it loads it for the grid provided
        else:
            self.grid_from_input(grid)
        
    #Works out the number of neighbours for a given square
    def no_of_neighbours(self, x, y):
        neighbours = 0
        #TODO Review if this should include diagonals - JC
        #Some patterns that should work with this, it could ether be due to this
        #Or my logic somewhere else is floored 
        
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

        #Checks diagonals
        if(y-1 >= 0 and x-1 >= 0):
            if(self.grid[x-1][y-1].get_is_alive()):
                neighbours += 1
        
        if(y-1 >= 0 and x +1 < self.length):
            if(self.grid[x+1][y-1].get_is_alive()):
                neighbours += 1
        
        if(y +1 < self.length and x -1 >= 0):
            if(self.grid[x-1][y+1].get_is_alive()):
                neighbours += 1
        
        if(y + 1 < self.length and x + 1 < self.length):
            if(self.grid[x+1][y+1].get_is_alive()):
                neighbours += 1

        return neighbours

    #Advances the board one unit of time and returns the changes
    def tick(self):
        changes = []
        for y in range(0 , self.length):
            for x in range(0, self.width):
                neighbours = self.no_of_neighbours(x ,y)
                if(neighbours == 3):
                    if(not self.grid[x][y].get_is_alive()):
                        self.grid[x][y].revive()
                        changes.append(Cords(x, y, "Add"))
                elif(neighbours != 2):
                    if(self.grid[x][y].get_is_alive()):
                        self.grid[x][y].kill()
                        changes.append(Cords(x, y, "Remove"))
        
        return changes

    #Creates a board based on a grid provided
    def grid_from_input(self, user_grid):
        self.grid = [[Square(False) for j in range(self.length)] for i in range(self.width)]
        for y in range(0, self.width):
            for x in range(0, self.length):
                if(user_grid[x][y]):  
                    self.grid[x][y].revive()

    #Returns grid
    def get_grid(self):
        return self.grid

    #Returns the width of the board
    def get_width(self):
        return self.width

    #Returns the length of the board
    def get_length(self):
        return self.length

    def revive_square(self, x, y):
        self.grid[x][y].revive

    def is_sq_alive(self, x, y):
        return self.grid[x][y].get_is_alive()
   
