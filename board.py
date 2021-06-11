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

    def change_cell_state(self):from square import Square
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