from tkinter import *
from functools import partial


class Grid_gui:

    def __init__(self):        
        self.settings()
        self.square_picker()
        self._root = Tk()
        self._root.title("Conways Game of Life")
        #self.window_width = str(self.grid_width *self.rect_size)
        #self.window_height = str(self.grid_length *self.rect_size)
        #self.window_size = (self.window_width+'x'+self.window_height)  
        #print('window size =',self.window_size)

        
    def create_grid(self,grid,grid_width,grid_length):
        
        self.board_frame = Frame(self._root)
        self.grid = grid
        self.grid_width = grid_width
        self.grid_length = grid_length
        self.rect_list = [["" for j in range(self.grid_length)] for i in range(self.grid_width )]
        self.canvas = Canvas(self.board_frame,width=self.grid_width *self.rect_size, height=self.grid_length*self.rect_size)
       
        x_coord = 0
        y_coord = 0 

        for y in range(0 ,self.grid_length):
            for x in range(0, self.grid_width ):

                rectangle = self.canvas.create_rectangle(x_coord, y_coord, x_coord+self.rect_size, y_coord+self.rect_size, fill = "White", outline = 'grey',width=1)
                #self.canvas.tag_bind('on_user_click',"<Button-1>",change_cell_state)
                self.rect_list[x][y] = rectangle
             
                if(self.grid[x][y].get_is_alive()):
                    self.canvas.itemconfig(rectangle,fill="White")
                else:
                    self.canvas.itemconfig(rectangle,fill="Black")

                x_coord += self.rect_size
            
                if x_coord >= self.grid_width*self.rect_size:
                    y_coord += self.rect_size
                    x_coord = 0 

            self.canvas.pack()

            self.board_frame.pack()

    def update_gui(self):

        for y in range(0 ,self.grid_length):
            for x in range(0, self.grid_width ):
                rectangle = self.rect_list[x][y]

                if(self.grid[x][y].get_is_alive()):
                    self.canvas.itemconfig(rectangle,fill="white")
                else:
                    self.canvas.itemconfig(rectangle,fill="Black")

        self.canvas.pack()
        self.board_frame.update()

        
    def settings(self):
        
        self.settings_win = Tk()
        self.settings_win.title('settings')
        sframe =Frame(self.settings_win)
        sframe.pack()
        
        w_label = Label(sframe,text='set board width')
        w_label.pack()
        self.width_entry = Entry(sframe)
        self.width_entry.insert(-1,10)
        self.width_entry.pack()

        l_label = Label(sframe,text='set board length')
        l_label.pack()
        self.length_entry = Entry(sframe)
        self.length_entry.insert(-1,10)
        self.length_entry.pack()

        s_label = Label(sframe,text='set rectangle size')
        s_label.pack()
        self.size_entry = Entry(sframe)
        self.size_entry.insert(-1,10)
        self.size_entry.pack()

        button = Button(sframe,text='confirm settings',command=self.confirm_settings)
        button.pack()
        self.settings_win.mainloop()

    def confirm_settings(self):
        #ToDo add catch incase of input not being an int
        self.grid_width = int(self.width_entry.get())
        self.grid_length = int(self.length_entry.get())
        self.rect_size = int(self.size_entry.get())
        self.temp_grid = [[False for j in range(self.grid_length)] for i in range(self.grid_width )]
        self.settings_win.destroy()
        
    def get_width(self):
        return self.grid_width
    
    def get_length(self):
        return self.grid_length

    def change_cell_state(self, x,y ):
        if(self.temp_grid[x][y]):
            self.temp_grid[x][y] = False
        else:
            self.temp_grid[x][y] = True
        print(x, y)
        print(self.temp_grid)

    def square_picker(self):
        #ToDo put  in a frame
        #creates tkinter gui grid on a canvas

    
        root = Tk()
        root.title("Conways Game of Life")
        canvas = Canvas(root, width=800, height=800)

        for y in range(0, self.grid_width):
            for x in range(0, self.grid_length):
                
                if(self.temp_grid[x][y]):
                    Button(canvas, text=str(x)+","+str(y), command=lambda r=y ,c=x, : self.change_cell_state(c, r), bg="green").grid(row=x,column=y)
                else:
                    Button(canvas, text=str(x)+","+str(y), command=lambda r=y ,c=x, : self.change_cell_state(c, r), bg="red").grid(row=x,column=y)
        canvas.pack()
        root.mainloop()

