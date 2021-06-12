from tkinter import *
import time

class Grid_gui:
    def __init__(self, master):
        self.master = master
        master.title("Conways Game of Life")

        self.frame = Frame(master,width=600,height=600)
        self.canvas = Canvas(master,width=800, height=800)
        self.canvas.pack()
        self.frame.pack()
    
        

    def create_grid(self,grid):

        #rectangle size
        rect_size = 25

        x_coord = 0
        y_coord = 0 

        self.canvas.create_rectangle(50,50,100,100,fill='black')
        self.canvas.pack()
        
        grid_length = grid(input)
        grid_width = map(len,input)
        for y in range(0 ,grid_length):
            for x in range(0, grid_width):

                #create 2darray to store rect
                rect = self.canvas.create_rectangle(x_coord, y_coord, x_coord+rect_size, y_coord+rect_size, fill = "White", outline = 'black',width=1,tags="on_user_click")
                
                #onclicklistner
                #self.canvas.tag_bind('on_user_click',"<Button-1>",change_cell_state)   
                
                if(grid[x][y].get_is_alive()):
                    self.canvas.itemconfig(rect,fill="Green")
                else:
                    self.canvas.itemconfig(rect,fill="Red")

                x_coord += rect_size

                        

                if x_coord >= grid_width*rect_size:
                    y_coord += rect_size
                    x_coord = 0 
            self.canvas.pack()




        def update_gui(self):
                for y in range(0 , self.length):
                            for x in range(0, self.width):
                                rect = self.rect_array[0][0]
                                print(rect)

                                if(self.grid[x][y].get_is_alive()):
                                    print("array index",self.grid[x][y])
                                    self.canvas.itemconfig(rect,fill="Green")
                                else:
                                    self.canvas.itemconfig(rect,fill="Red")
                                self.rect_array.insert(x,y,rect)
                                self.canvas.pack()

        
        

root = Tk()
my_gui = Grid_gui(root)
root.mainloop()