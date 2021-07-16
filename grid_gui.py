from random import Random, randint
from boards import Board_Type
from board import Board
from cords import Cords
from tools import get_patterns, load_patterns
import pygame
import pygame_menu
import sys
import asyncio

sys.path.insert(1, 'data/')
from colours import *
#TODO Work out why it looks different when picking squares compaired to when the game is actually running

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
        self.temp_grid = [[False for j in range(width)] for i in range(height)]
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
                    if(x <= display_width):
                        #Works out col and row and add this to changes to update visual board
                        real_x, real_y = x//sq_size, y//sq_size
                        print(real_x,real_y)
                        changes.append(Cords(real_x, real_y, "Add"))
                        #Revives the sqaure at the given pos in the logical grid
                        #TODO This will need to changed
                        self.temp_grid[real_x][real_y] = True
                    elif(x > display_width):
                        print(y)
                        if (y >= 10 and y <= 40):
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
                        elif ( y >= 50 and y <= 80):
                            type = Board_Type['user']
                            board = Board(width, height, self.temp_grid, type)
                            self.grid = board.get_grid()
                            self.grid_width = board.get_width()
                            self.grid_length = board.get_length()
                            self.playing = True
                            self.load_sq()
                            print(type)
                        elif(y >=80 and y <= 100):
                            self.draw_pattern()

                    
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

        img2 = font.render('User Input', True, blue)
        self.screen.blit(img2, (display_width+10, 50))

        img3 = font.render('Patterns', True, blue)
        self.screen.blit(img3, (display_width+10, 80))


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

    def draw_pattern(self):
        #TODO mouse x,y + pattern coord, if pattern coord is > or < grid x,y dont draw

        load_patterns()
        patterns = get_patterns()
        pattern_coords = []

       
        print(patterns[0].get_pattern_name())
        print(patterns[0].get_pattern_pattern().split(","))

        pattern_coords = patterns[0].get_pattern_pattern().split(",")
       
        # for loop for coords list
        for i in range(len(pattern_coords) -1 ):  

            #current coords
            print("coord",i,pattern_coords[i])
            x = pattern_coords[i]
            y = pattern_coords[i+1]        
            self.draw_sq(int(x)*sq_size,int(y)*sq_size,alive_colour)
            


if __name__ == "__main__":
    asyncio.run(main())