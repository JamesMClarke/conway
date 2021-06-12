from tkinter import *
import time

root = Tk()
    
       
    
    

def create_grid(grid,grid_width, grid_length ):
    #rectangle size
    rect_size = 25
    canvas = Canvas(root,width=grid_width*rect_size, height=grid_length*rect_size)
    canvas.pack()
  
    x_coord = 0
    y_coord = 0 


    
    rect_array = [grid_width][grid_length]

    for y in range(0 ,grid_length):
        for x in range(0, grid_width):
                #create 2darray to store rect
            rect = canvas.create_rectangle(x_coord, y_coord, x_coord+rect_size, y_coord+rect_size, fill = "White", outline = 'black',width=1,tags="on_user_click")
            #rect_array[x][y].append(rect)
            #print("rect array index",rect_array[x][y])  
                #onclicklistner
                #canvas.tag_bind('on_user_click',"<Button-1>",change_cell_state)   
                
            if(grid[x][y].get_is_alive()):
                canvas.itemconfig(rect,fill="Green")
            else:

                canvas.itemconfig(rect,fill="Red")

            x_coord += rect_size

                        

            if x_coord >= grid_width*rect_size:
                y_coord += rect_size
                x_coord = 0 
        canvas.pack()




        def update_gui(self):
                for y in range(0 , length):
                            for x in range(0, width):
                                rect = rect_array[0][0]
                                print(rect)

                                if(grid[x][y].get_is_alive()):
                                    print("array index",grid[x][y])
                                    canvas.itemconfig(rect,fill="Green")
                                else:
                                    canvas.itemconfig(rect,fill="Red")
                                rect_array.insert(x,y,rect)
                                canvas.pack()

    root.geometry('300x800')
    root.title("Conways Game of Life")
 
    root.mainloop()