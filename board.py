from square import Square
import random
from tkinter import *

def main():
    board = Board()
    board.tick()
    print()
    board.print_new()

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
    
   def grid_gui(self):
        #ToDo put  in a frame
        #ToDo allow user to change state of cell
        #ToDo add user configurable sizing and colouring of rectangles
        #creates tkinter gui grid on a canvas

    
        root = Tk()
        root.title("Conways Game of Life")


        self.canvas = Canvas(root, width=800, height=800)
        x_coord = 0
        y_coord = 0 

        #adjust value to change rect size
        rect_size = 50
        #loops through grid array
        for i in self.grid:
            for j in i:

                rect = self.canvas.create_rectangle(x_coord, y_coord, x_coord+rect_size, y_coord+rect_size, fill = "White", outline = 'black',width=1, tags ="setStateButton")

                if(j.get_is_alive()):
                    #self.canvas.create_rectangle(x_coord, y_coord, x_coord+rect_size, y_coord+rect_size, fill = "Green", outline = 'black',width=1, tags ="setStateButton")
                    self.canvas.itemconfig(rect,fill="Green")
                    #self.canvas.tag_bind("setStateButton","<Button-1>",self.change_cell_state)
                else:
                    self.canvas.itemconfig(rect,fill="Red")
                    #self.canvas.tag_bind("setStateButton","<Button-1>",self.change_cell_state)

                x_coord = x_coord + rect_size

                    

                #if x_coord is >= than grid width * rect width, increments y_coord by itself plus rect width. resets x_coord coord
                if x_coord >= self.width*rect_size:
                    y_coord = y_coord+rect_size
                    x_coord = 0 
                self.canvas.pack()


                
                
        root.mainloop()

    def change_cell_state(self):

        print("Code for cell state change goes here")

    def update_board():



if __name__ == "__main__":
    main()
