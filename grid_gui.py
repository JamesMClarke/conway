from boards import Board_Type
from board import Board
from cords import Cords
import tools
import pygame
import sys
sys.path.insert(1, 'data/')
from colours import *

#Board setttings
sq_size = 20
width = 20
height = 20
line_size = 1
display_width = width * sq_size
full_display_width = display_width + 200
display_height = height * sq_size

#Colour settings
backgroup_colour = white
line_colour = black
sq_colours = [blue,black,red,orange,yellow,green,sky_blue]
dead_colour = backgroup_colour
game_over_background_colour = gray
game_over_text_colour = white

#Text settings
font_size = 30
end_game_font_size = 50

#Loaded from json
patterns = tools.load_patterns()

def main():
    gui =  Grid_gui()

class Grid_gui:
    def __init__(self):        
        
        pygame.init()

        #Variables which will change during the game
        user_placing_pattern = False
        self.user_picking = True
        self.playing = False
        self.temp_grid = [[False for j in range(width)] for i in range(height)]
        self.screen = pygame.display.set_mode((full_display_width,display_height))
        self.screen.fill(backgroup_colour)
        #default pattern selected
        self.current_pattern = 0
        self.count = 0
        #default alive colour - SC
        self.alive_colour = sq_colours[0]

        #temp blank vars        
        changes = []
        
        #Draws grid
        self.drawGrid() 

        while True:
            #Draws square to show alive colour
            self.draw_sq(display_width+10,100,self.alive_colour)
            
            font = pygame.font.SysFont(None, font_size)
            img7 = font.render(patterns[self.current_pattern].get_pattern_name(),True,blue) 
            self.screen.blit(img7,(display_width+30,150))

            if self.playing:
                #Wait timer to slow down the game
                pygame.time.wait(1000)
                #Moves the board forward one cycle and saves the changes
                changes = self.board.tick()
                
                #If there aren't any changes it then renders a game over screen
                if(len(changes) == 0):
                    #TODO Add reset button - JC
                    #Renders game over screen
                    rect =  pygame.Rect(0,0,full_display_width,display_height)
                    pygame.draw.rect(self.screen,game_over_background_colour,rect)
                    font = pygame.font.SysFont(None, end_game_font_size)
                    game_over = font.render('Game over', True, game_over_text_colour)
                    text_rect = game_over.get_rect(center=(full_display_width//2, display_height//2))
                    self.screen.blit(game_over, text_rect)

            for event in pygame.event.get():

                #Listens for mouse event
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()

                    #If the x cord is within the grid
                    if(x <= display_width):

                        #Works out col and row
                        real_x, real_y = x//sq_size, y//sq_size

                        #If the user has already clicked the pattern button
                        if(user_placing_pattern):
                            #TODO Double check that this doesn't interfear with game logic - JC
                            #Places the patten at the x and y the user has just clicked
                            self.get_pattern(real_x, real_y)

                            #I'm pretty sure we could just define board as self.board
                            #And then call that rather than having grid as a thing
                            self.board = Board(width, height, self.temp_grid, type)
                            
                            #Sets playing to be true
                            self.playing = True

                            #Loads grid from board
                            self.load_sq()    
                        
                        #Otherwise the user is placing an individual square
                        else:
                            #Adds the change to the list
                            changes.append(Cords(real_x, real_y, "Add"))
                            #Revives the square at the given pos in the logical grid
                            self.temp_grid[real_x][real_y] = True
                        
                    #If the mouse event is on the settings panel
                    elif(x > display_width):     
                        #Handles mouse for random button
                        if (y >= 10 and y <= 40):
                                #Sets type to enum
                                type = Board_Type['random']
                                #Creates a blank grid 
                                grid =""
                                #Creates a board
                                self.board = Board(width, height, grid, type)
                                
                                self.playing = True
                                self.load_sq()                                
                                print(type)
                        elif ( y >= 50 and y <= 80):
                                type = Board_Type['user']
                                self.board = Board(width, height, self.temp_grid, type)
                                self.playing = True
                                self.load_sq()
                                print(type)
                        
                        #If the alive colour button is pressed calls sq_colour
                        elif(y >=80 and y <= 100):
                            self.alive_colour = self.sq_colour()


                        #sets placement of pattern to true
                        elif((y >= 140 and y<=160) and (x >= display_height+20 and x <= display_width+150)):
                            type = Board_Type['pattern'] 
                            user_placing_pattern = True
                           
                        #Mouse events for pattern select
                        #TODO fix bug of pattern name overwriting previous pattern name -SC
                        elif((y >= 140 and y<=160) and (x >= display_width+10 and x <= display_width+20)):
                            print("<")
                            self.current_pattern = self.current_pattern-1
                            self.set_current_pattern()

                        elif((y >= 140 and y<=160) and (x >= display_width+150 and x <= display_width+170)):
                            print(">")
                            self.current_pattern = self.current_pattern+1
                            self.set_current_pattern()


    
                    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.update_by_changes(changes)
            pygame.display.update()

       
    #Draws the grid
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

        img5 = font.render('<',True,blue) 
        self.screen.blit(img5,(display_width+10,150))

        img6 = font.render('>',True,blue) 
        self.screen.blit(img6,(display_width+150,150))
        


    #Increments colour
    def sq_colour(self):

        if(self.count > len(sq_colours)-2):
            self.count = 0
        else:
            self.count += 1
        colour = sq_colours[self.count]
                           
        return colour

    #Loads board onto the grid
    def load_sq(self):
        for y in range(0 ,self.board.get_width()):
            for x in range(0, self.board.get_length()):
                if(self.board.is_sq_alive(x, y)):
                    colour  = self.alive_colour
                else:
                    colour  = dead_colour
                self.draw_sq(x*sq_size,y*sq_size,colour)

    #Updates the board based on the changes
    def update_by_changes(self, changes):
        for c in changes:
            x, y, change = c.get_cords()
            print(x, y)
            if(change == "Add"):
                colour = self.alive_colour            
            else:
                colour = dead_colour
            self.draw_sq(x*sq_size,y*sq_size,colour)

    #Draws square 
    def draw_sq(self,x,y,colour):
        rect =  pygame.Rect(x+line_size,y+line_size,sq_size-line_size,sq_size-line_size)
        pygame.draw.rect(self.screen,colour,rect)
    
    #Sets current pattern based upon pattern name
    #TODO get rid of hard coded variable - SC
    #TODO pass to get_pattern - SC
    def set_current_pattern(self):

        if(self.current_pattern < 0 or self.current_pattern > len(patterns)-1) :
            self.current_pattern = 0 
        print("set pattern test",patterns[self.current_pattern].get_pattern_pattern())
    
    #Places pattern on the temp grid
    def get_pattern(self, x, y):
        #TODO add pattern selection option - SC
        #TODO Add more patterns - SC
        pattern_coords = []
        pattern_coords = patterns[self.current_pattern].get_pattern_pattern().split(",")      
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