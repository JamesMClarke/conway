from square import Square
from cords import Cords
    
class Board:
    def __init__(self, grid):
        self.__width = len(grid)
        self.__height = len(grid[0])
        self.__neighbours = [[0 for j in range(self.__height)] for i in range(self.__width)]
        #Loads it for the __grid provided
        
        self.grid_from_input(grid)

    #Works out the number of ____neighbours for a given square
    def no_of___neighbours(self, x, y):
        n = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                #print(x, y)
                x_check = x + i
                y_check = y + j
                if(not( i == 0 and j == 0) and (x_check > 0 and x_check <= self.__width-1 and y_check > 0 and y_check <= self.__height-1)):
                    if(self.__grid[x_check][y_check].get_is_alive()):
                        n += 1
        return n

    #Advances the board one unit of time and returns the changes
    def tick(self):
        changes = []
        for y in range(0 , self.__height):
            for x in range(0, self.__width):
                n = self.no_of___neighbours(x ,y)
                self.__neighbours[x][y] = n
                if(n == 3):
                    if(not self.__grid[x][y].get_is_alive()):
                        changes.append(Cords(x, y, "Add"))
                elif(n != 2):
                    if(self.__grid[x][y].get_is_alive()):
                        changes.append(Cords(x, y, "Remove"))

        #Applies changes after the board is checked
        self.apply_changes(changes)
        return changes

    def apply_changes(self, changes):
        for c in changes:
            x, y, change = c.get_cords()
            if(change == "Add"):
                self.__grid[x][y].revive()
            else:
                self.__grid[x][y].kill()

    #Creates a board based on a __grid provided
    def grid_from_input(self, user___grid):
        self.__grid = [[Square(False) for j in range(self.__height)] for i in range(self.__width)]
        for y in range(0, self.__height):
            for x in range(0, self.__width):
                if(user___grid[x][y]):  
                    self.__grid[x][y].revive()

    #Returns __grid
    def get_grid(self):
        return self.__grid

    #Returns the __width of the board
    def get_width(self):
        return self.__width

    #Returns the __height of the board
    def get_height(self):
        return self.__height

    def revive_square(self, x, y):
        self.__grid[x][y].revive

    def is_sq_alive(self, x, y):
        return self.__grid[x][y].get_is_alive()
   
