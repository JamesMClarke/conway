from square import Square
from boards import Board_Type
from random import getrandbits
from cords import Cords
    
class Board:
    #Add enum ext
    #Make user grid
    def __init__(self, width, length, grid, type):
        self.length = length
        self.width = width
        if(type == Board_Type['user'] or type == Board_Type['pattern']):
            self.grid_from_input(grid)
        elif(type == Board_Type['random']):
            #Creates a random grid
            self.grid = [[Square(bool(getrandbits(1))) for j in range(self.length)] for i in range(self.width)]

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

    def grid_from_input(self, user_grid):
        self.grid = [[Square(False) for j in range(self.length)] for i in range(self.width)]
        print(user_grid)
        for y in range(0, self.width):
            for x in range(0, self.length):
                if(user_grid[x][y]):  
                    print("Reviving ", x, y)
                    self.grid[x][y].revive()


    def get_grid(self):
        return self.grid

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def revive_square(self, x, y):
        self.grid[x][y].revive
   
