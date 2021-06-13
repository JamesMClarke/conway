from tkinter import *
import time

root = Tk()


    
class Grid_gui:
    def __init__(self,grid,grid_width,grid_length):
        
        self.grid = grid
        self.grid_width = grid_width
        self.grid_length = grid_length

        self.rect_size = 25

        self.window_width = str(self.grid_width *self.rect_size)
        self.window_height = str(self.grid_length *self.rect_size)
        self.window_size = (self.window_width+'x'+self.window_height)
        print('window size =',self.window_size)
        create_grid(self)



def create_grid(self):
    #rectangle size
    


    canvas = Canvas(root,width=self.grid_width *self.rect_size, height=self.grid_length*self.rect_size)
    canvas.pack()
  
    x_coord = 0
    y_coord = 0 

    #2dlist of rectangles
    self.rect_list = [["" for j in range(self.grid_length)] for i in range(self.grid_width )]

    

    for y in range(0 ,self.grid_length):
        for x in range(0, self.grid_width ):

            rect = canvas.create_rectangle(x_coord, y_coord, x_coord+self.rect_size, y_coord+self.rect_size, fill = "White", outline = 'grey',width=1,tags="on_user_click")
            #canvas.tag_bind('on_user_click',"<Button-1>",change_cell_state)   
                
            if(self.grid[x][y].get_is_alive()):
                canvas.itemconfig(rect,fill="White")
            else:
                canvas.itemconfig(rect,fill="Black")

            x_coord += self.rect_size
            #add rectangles to rect_list
            self.rect_list[x][y] = rect

                        

            if x_coord >= self.grid_width*self.rect_size:
                y_coord += self.rect_size
                x_coord = 0 
        canvas.pack()



        def update_gui(self,rect_list):
                for y in range(0 , self.grid_length):
                            for x in range(0, self.grid_width):
                                rect = self.rect_array[0][0]
                                print(rect)

                                if(self.grid[x][y].get_is_alive()):
                                    print("array index",self.grid[x][y])
                                    canvas.itemconfig(rect,fill="Green")
                                else:
                                    canvas.itemconfig(rect,fill="Red")
                                canvas.pack()

    root.geometry(self.window_size)
    root.title("Conways Game of Life")
 
    root.mainloop()

