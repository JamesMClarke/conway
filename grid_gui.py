from tkinter import *
import time

root = Tk()
#ToDo Update method find away to access rectangles for reference
#ToDo add options menu


    
class Grid_gui:
    def __init__(self,grid,grid_width,grid_length):
        
        self.grid = grid
        self.grid_width = grid_width
        self.grid_length = grid_length

        self.rect_size = 15
        self.rect_list = [["" for j in range(self.grid_length)] for i in range(self.grid_width )]

        #self.canvas = Canvas(root,width=self.grid_width *self.rect_size, height=self.grid_length*self.rect_size)

        self.window_width = str(self.grid_width *self.rect_size)
        self.window_height = str(self.grid_length *self.rect_size)
        self.window_size = (self.window_width+'x'+self.window_height)
        print('window size =',self.window_size)




    def create_grid(self):
        

        
        self.canvas = Canvas(root,width=self.grid_width *self.rect_size, height=self.grid_length*self.rect_size)

        x_coord = 0
        y_coord = 0 

        for y in range(0 ,self.grid_length):
            for x in range(0, self.grid_width ):


                rectangle = self.canvas.create_rectangle(x_coord, y_coord, x_coord+self.rect_size, y_coord+self.rect_size, fill = "White", outline = 'grey',width=1)
                #self.canvas.tag_bind('on_user_click',"<Button-1>",change_cell_state)
                self.rect_list[x][y] = rectangle
                print('rect',self.rect_list[0][0]) 
            
   
                    
                if(self.grid[x][y].get_is_alive()):
                    self.canvas.itemconfig(rectangle,fill="White")
                else:
                    self.canvas.itemconfig(rectangle,fill="Black")


                x_coord += self.rect_size
            
                if x_coord >= self.grid_width*self.rect_size:
                    y_coord += self.rect_size
                    x_coord = 0 

            self.canvas.pack()
        self.show_board()


    def show_board(self):

        root.geometry(self.window_size)
        root.title("Conways Game of Life")
        
        root.mainloop()



    def update_gui(self):
        rectangle = self.rect_list[1][5]
        self.canvas.itemconfigure(rectangle,fill='green')
        self.canvas.pack()

      
       


   

