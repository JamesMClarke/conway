from random import Random, randint
from boards import Board_Type
from board import Board
from cords import Cords
import pygame
import pygame_menu
import sys
import asyncio

sys.path.insert(1, 'data/')
from colours import *
#TODO in check neighbours if state is changed pass to list and pass to update   

sq_size = 20
width = 20
height = 20
backgroup_colour = white
line_colour = black
alive_colour = blue
dead_colour = backgroup_colour
line_size = 1
display_width = width * sq_size
display_height = height * sq_size
user_picking = False

#TODO add menu's for pattern placement 
async def main():
    gui =  Grid_gui()

class Grid_gui:

    def __init__(self):        
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((display_width,display_height))
        self.screen.fill(backgroup_colour)
        #temp blank vars
        grid =""
        type = Board_Type['random']
        board = Board(width, height, grid, type)
        self.grid = board.get_grid()
        self.grid_width = board.get_width()
        self.grid_length = board.get_length()
        #settings is commented out as it does nothing atm
        #self.settings_menu()
        self.drawGrid() 
        changes = []
        while True:                               
            if not user_picking:
                #await asyncio.sleep(1)
                pygame.time.wait(1000)
                changes = board.tick()

            for event in pygame.event.get():
                # handle MOUSEBUTTONUP
                #If the use is still picking
                if(user_picking):
                    #Listens for mose event
                    if event.type == pygame.MOUSEBUTTONUP:
                        x,y = pygame.mouse.get_pos()
                        #Works out col and row and add this to changes to update visual board
                        print(x//sq_size, y//sq_size)
                        changes.append(Cords(x//sq_size, y//sq_size, "Add"))
                        #Revives the sqaure at the given pos in the logical grid
                        grid.revive_square(x, y)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.update_by_changes(changes)
            pygame.display.update()

       

    def drawGrid(self):
        
        for x in range (0,width*sq_size,sq_size):
            for y in range (0,height*sq_size,sq_size):
                rect =  pygame.Rect(x,y,sq_size,sq_size)
                pygame.draw.rect(self.screen,line_colour,rect,line_size)
        if(not user_picking):
            for y in range(0 ,self.grid_length):
                for x in range(0, self.grid_width):
                    if(self.grid[x][y].get_is_alive()):
                        colour  = alive_colour
                    else:
                        colour  = dead_colour
                    self.draw_sq(x*sq_size,y*sq_size,colour)


    def update_by_changes(self, changes):
        for c in changes:
            x, y, change = c.get_cords()
            print(x, y)
            if(change == "Add"):
                colour = alive_colour            
            else:
                colour = dead_colour
            self.draw_sq(x*sq_size,y*sq_size,colour)

        #draws square 
    def draw_sq(self,x,y,colour):
        #print(x/sq_size,y/sq_size,colour)
        rect =  pygame.Rect(x,y,sq_size-line_size,sq_size-line_size)
        pygame.draw.rect(self.screen,colour,rect)

    #TODO add input for gird size, sq size and dead and alive sq colour select
    #TODO add menu for user picking of squares
    def settings_menu(self):
        menu = pygame_menu.Menu('Game Settings',display_width,display_height,theme=pygame_menu.themes.THEME_BLUE)
        menu.add.button('quit',pygame_menu.events.EXIT)
        menu.mainloop(self.screen)

    def set_grid_size(self, a):
        self.grid_length = a
        print (a)


if __name__ == "__main__":
    asyncio.run(main())