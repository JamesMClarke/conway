from boards import Board_Type
from board import Board
from cords import Cords
import tools
import pygame
import sys
patterns = tools.load_patterns()


sys.path.insert(1, 'data/')
from colours import *

#Settings
sq_size = 20
width = 20
height = 20
backgroup_colour = white
line_colour = black
sq_colours = [blue,black,red,orange,yellow,green,sky_blue]
dead_colour = backgroup_colour
line_size = 1
display_width = width * sq_size
full_display_width = display_width + 200
display_height = height * sq_size
font_size = 30

def main():
    gui =  Grid_gui()

class Grid_gui:

    def __init__(self):        
        
        pygame.init()


        #Variables which will change during the game
        self.user_picking = True
        self.playing = False
        self.temp_grid = [[False for j in range(width)] for i in range(height)]
        self.screen = pygame.display.set_mode((full_display_width,display_height))
        self.screen.fill(backgroup_colour)
        #default pattern selected - SC
        self.current_pattern = 0
        self.count = 0
        #default alive colour - SC
        self.alive_colour = sq_colours[0]
        #temp blank vars        
        self.drawGrid() 
        changes = []
        user_placing_pattern = False
        while True:
            self.draw_sq(display_width+10,100,self.alive_colour)

                               
            if self.playing:
                #await asyncio.sleep(1)
                pygame.time.wait(1000)
                changes = board.tick()
                if(len(changes) == 0):
                    #TODO Add game over screen and reset ready for next name - JC
                    print("game over")
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
                        #If the user has already clicked the pattern button
                        if(user_placing_pattern):
                            #TODO Double check that this doesn't interfear with game logic - JC
                            #Places the patten at the x and y the user has just clicked
                            self.get_pattern(real_x, real_y)
                            board = Board(width, height, self.temp_grid, type)
                            self.grid = board.get_grid()
                            self.grid_width = board.get_width()
                            self.grid_length = board.get_length()
                            self.playing = True
                            self.load_sq()    
                            print(real_x,real_y)
                        else:
                            changes.append(Cords(real_x, real_y, "Add"))
                            #Revives the sqaure at the given pos in the logical grid
                            self.temp_grid[real_x][real_y] = True
                        
                    elif(x > display_width):                            
                        print(y)
                        if (y >= 10 and y <= 40):
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
                            self.alive_colour = self.sq_colour()



                        elif(y >= 110 and y<=130):
                            self.set_current_pattern()
                            type = Board_Type['pattern'] 
                            user_placing_pattern = True
                           
                        #TODO add mouse events for each pattern here - SC
    
                    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.update_by_changes(changes)
            pygame.display.update()

       

    def drawGrid(self):
        
        for x in range (0,display_width,sq_size):
            print("looping")
            for y in range (0,display_height,sq_size):
                rect =  pygame.Rect(x,y,sq_size+1,sq_size+1)
                pygame.draw.rect(self.screen,line_colour,rect,line_size)

        font = pygame.font.SysFont(None, font_size)
        img = font.render('Random', True, blue)
        self.screen.blit(img, (display_width+10, 20))

        img2 = font.render('User Input', True, blue)
        self.screen.blit(img2, (display_width+10, 50))

        img3 = font.render('Cycle Alive Colour', True, blue)
        self.screen.blit(img3, (display_width+10, 80))
        
        img4 = font.render('Patterns', True, blue)
        self.screen.blit(img4, (display_width+10, 120))
        
        #TODO change to cycle through patterns instead of displaying all of them - SC
        pattern_start = 150
        for i in range(0, len(patterns)):
            print("pattern name ", patterns[i].get_pattern_name())
            img5 = font.render( str(patterns[i].get_pattern_name()), True, blue)
            self.screen.blit(img5, (display_width+10, pattern_start))
            pattern_start = pattern_start + 30


    #changes colour
    def sq_colour(self):

        if(self.count > len(sq_colours)-2):
            self.count = 0
        else:
            self.count += 1
        colour = sq_colours[self.count]
                           
        return colour




    def load_sq(self):
        for y in range(0 ,self.grid_length):
            for x in range(0, self.grid_width):
                if(self.grid[x][y].get_is_alive()):
                    colour  = self.alive_colour
                else:
                    colour  = dead_colour
                self.draw_sq(x*sq_size,y*sq_size,colour)


    def update_by_changes(self, changes):
        for c in changes:
            x, y, change = c.get_cords()
            print(x, y)
            if(change == "Add"):
                colour = self.alive_colour            
            else:
                colour = dead_colour
            self.draw_sq(x*sq_size,y*sq_size,colour)

        #draws square 
    def draw_sq(self,x,y,colour):
        #print(x/sq_size,y/sq_size,colour)
        rect =  pygame.Rect(x+line_size,y+line_size,sq_size-line_size,sq_size-line_size)
        pygame.draw.rect(self.screen,colour,rect)
    
    #sets current pattern based upon pattern name - SC
    #TODO get rid of hard coded variable - SC
    #TODO pass to get_pattern - SC
    def set_current_pattern(self):
        pattern = 'test'

        for i in range(0, len(patterns)):
            if(patterns[i].get_pattern_name() == pattern):
                print("set pattern test",patterns[i].get_pattern_pattern())
                current_pattern = i 
    
    def get_pattern(self, x, y):
        
        #TODO add pattern selection option - SC
        #TODO Add more patterns - SC
        #patterns = tools.load_patterns()
        pattern_coords = []
        pattern_coords = patterns[1].get_pattern_pattern().split(",")      
        # for loop for coords list
        for i in range(0, len(pattern_coords) -1, 2):  
            print(i)
            #current coords
            #print("coord",i,pattern_coords[i])
            x = int(pattern_coords[i]) + x
            y = int(pattern_coords[i+1]) + y 
            print("Pattern" , x, y)
            if(x < (width - 1) and y < (height - 1)):
                self.temp_grid[x][y] = True
                self.draw_sq(x,y,self.alive_colour)      


if __name__ == "__main__":
    main()