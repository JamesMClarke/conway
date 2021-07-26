from square import Square
from boards import Board_Type
from random import getrandbits
from cords import Cords
    
class Board:
    #TODO Make variables protected
    def __init__(self, width, length, grid, type):
        self.length = length
        self.width = width
        self.neighbours = [[0 for j in range(self.width)] for i in range(self.length)]
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
        for i in range(-1, 2):
            for j in range(-1, 2):
                #print(x, y)
                x_check = x + i
                y_check = y + j
                if(not( i == 0 and j == 0) and (x_check > 0 and x_check <= self.length-1 and y_check > 0 and y_check <= self.width-1)):
                    if(self.grid[x_check][y_check].get_is_alive()):
                        neighbours += 1
        return neighbours

    #Advances the board one unit of time and returns the changes
    def tick(self):
        changes = []
        for y in range(0 , self.length):
            for x in range(0, self.width):
                neighbours = self.no_of_neighbours(x ,y)
                self.neighbours[x][y] = neighbours
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
   
