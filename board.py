from square import Square
import random
from tkinter import *

def main():
    board = Board()
    board.print_grid()
    board.grid_gui()

class Board:
    width = 8
    length = 8

    def __init__(self):
        self.grid = [[Square(bool(random.getrandbits(1))) for j in range(self.width)] for i in range(self.length)]


    def print_grid(self):
        for x in self.grid:
            for y in x:
                if(y.get_is_alive()):
                    print("X", end ="|")
                else:
                    print("D", end ="|")
            print("")
            print("-".join(["-"] * self.width))


    def grid_gui(self):
        #ToDo adjust rect size 
        #creates tkinter gui grid on a canvas

    
        root = Tk()
        self.grid_canvas = Canvas(root, width=800, height=800)
        x_coord = 0
        y_coord = 0 

        for x in self.grid:
            for y in x:
                # start new line if greater than width

                if(y.get_is_alive()):
                    #coordinates squares are overwiring one another
                    self.grid_canvas.create_rectangle(x_coord, y_coord, x_coord+25, y_coord+25, fill = "Green", outline = 'black',width=1)
                else:
                    self.grid_canvas.create_rectangle(x_coord, y_coord, x_coord+25, y_coord+25, fill = "red", outline = 'black',width=1)
                x_coord = x_coord + 25


                #if x_coord is >= than grid width * rect width, increments y_coord by itself plus rect width. resets x_coord coord
                if x_coord >= self.width*25:
                    y_coord = y_coord+25
                    x_coord = 0 
                self.grid_canvas.pack()
                
                
        root.mainloop()
         


if __name__ == "__main__":
    main()