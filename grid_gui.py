from tkinter import *

#ToDo Update method find away to access rectangles for reference
#ToDo add options menu


    
class Grid_gui:
    def __init__(self,grid,grid_width,grid_length):
        self._root = Tk()
        self.label = Label(self._root, text="Conways Game of Life")
        self.label.pack()

        self.grid = grid
        self.grid_width = grid_width
        self.grid_length = grid_length

        self.rect_size = 15
        self.rect_list = [["" for j in range(self.grid_length)] for i in range(self.grid_width )]

        self.window_width = str(self.grid_width *self.rect_size)
        self.window_height = str(self.grid_length *self.rect_size)
        self.window_size = (self.window_width+'x'+self.window_height)  
        print('window size =',self.window_size)

        #To Do put menu in frame in main loop
        #Add funcs for options 
        menubar = Menu(self._root)
        options_menu = Menu(menubar, tearoff=0)
        options_menu.add_command(label="reload board", command="")
        options_menu.add_command(label="change board size", command="")
        options_menu.add_command(label="change rectangle size", command="")
        options_menu.add_separator()
        options_menu.add_command(label="Exit", command=self._root.destroy)
        menubar.add_cascade(label="Options", menu=options_menu)

        self._root.config(menu=menubar)


    def create_grid(self):
        self.canvas = Canvas(self._root,width=self.grid_width *self.rect_size, height=self.grid_length*self.rect_size)

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
            self._root.update()

    def update_gui(self):

        for y in range(0 ,self.grid_length):
            for x in range(0, self.grid_width ):
                rectangle = self.rect_list[x][y]

                if(self.grid[x][y].get_is_alive()):
                    self.canvas.itemconfig(rectangle,fill="white")
                else:
                    self.canvas.itemconfig(rectangle,fill="Black")

        self.canvas.pack()
        self._root.update()

      
       


   

