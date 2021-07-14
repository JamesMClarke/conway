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

#Settings
sq_size = 20
width = 20
height = 20
backgroup_colour = white
line_colour = black
alive_colour = blue
dead_colour = backgroup_colour
line_size = 1
display_width = width * sq_size
full_display_width = display_width + 200
display_height = height * sq_size
font_size = 30

#TODO add menu's for pattern placement 
async def main():
    gui =  Grid_gui()

class Grid_gui:

    def __init__(self):        
        
        pygame.init()


        #Variables which will change during the game
        self.user_picking = False
        self.playing = False
        
        self.screen = pygame.display.set_mode((full_display_width,display_height))
        self.screen.fill(backgroup_colour)
        #temp blank vars        
        #settings is commented out as it does nothing atm
        #self.settings_menu()
        self.drawGrid() 
        changes = []
        while True:                               
            if not self.user_picking and self.playing:
                #await asyncio.sleep(1)
                pygame.time.wait(1000)
                changes = board.tick()

            for event in pygame.event.get():
                # handle MOUSEBUTTONUP
                #Listens for mose event
                if event.type == pygame.MOUSEBUTTONUP:
                    #If the use is still picking
                    x,y = pygame.mouse.get_pos()
                    if(self.user_picking and x <= display_width):
                        #Works out col and row and add this to changes to update visual board
                        print(x//sq_size, y//sq_size)
                        changes.append(Cords(x//sq_size, y//sq_size, "Add"))
                        #Revives the sqaure at the given pos in the logical grid
                        #TODO This will need to changed
                        board.revive_square(x//sq_size, y//sq_size)
                    elif(x > display_width):
                        #TODO This need defining properly
                        #Handle mouse clicks on buttons
                        type = Board_Type['random']
                        grid =""
                        board = Board(width, height, grid, type)
                        self.grid = board.get_grid()
                        self.grid_width = board.get_width()
                        self.grid_length = board.get_length()
                        self.playing = True
                        self.load_sq()
                        print(type)
                    
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

        font = pygame.font.SysFont(None, font_size)
        img = font.render('Random', True, blue)
        self.screen.blit(img, (display_width+10, 20))


    def load_sq(self):
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