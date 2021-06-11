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
        #creates tkinter gui grid on a canvas

    
        root = Tk()
        root.title("Conways Game of Life")


        self.canvas = Canvas(root, width=800, height=800)
        x_coord = 0
        y_coord = 0 

        #adjust value to change rect size
        rect_size = 50

        for x in self.grid:
            for y in x:
                # start new line if greater than width
                rect = self.canvas.create_rectangle(x_coord, y_coord, x_coord+rect_size, y_coord+rect_size, fill = "White", outline = 'black',width=1, tags ="setStateButton")
                if(y.get_is_alive()):
                    #coordinates squares are overwiring one another
                    #self.canvas.create_rectangle(x_coord, y_coord, x_coord+rect_size, y_coord+rect_size, fill = "Green", outline = 'black',width=1, tags ="setStateButton")
                    self.canvas.itemconfig(rect,fill="Green")
                    self.canvas.tag_bind("setStateButton","<Button-1>",self.change_cell_state)

                else:
                    self.canvas.itemconfig(rect,fill="Red")

                    #self.canvas.create_rectangle(x_coord, y_coord, x_coord+rect_size, y_coord+rect_size, fill = "red", outline = 'black',width=1,tags ="setStateButton")
                    self.canvas.tag_bind("setStateButton","<Button-1>",self.change_cell_state)

                x_coord = x_coord + rect_size

                    

                #if x_coord is >= than grid width * rect width, increments y_coord by itself plus rect width. resets x_coord coord
                if x_coord >= self.width*rect_size:
                    y_coord = y_coord+rect_size
                    x_coord = 0 
                self.canvas.pack()


                
                
        root.mainloop()

    def change_cell_state(x,y):

        print("Code for cell state change goes here")


if __name__ == "__main__":
    main()