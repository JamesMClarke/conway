from boards import Board_Type
from board import Board
from cords import Cords
import tools
import pygame
import sys
sys.path.insert(1, 'data/')
from colours import *

#Enables and disables debug board
debug = False

#Board setttings
sq_size = 20
width = 70
height = 40
line_size = 1
display_width = width * sq_size
full_display_width = display_width + 300
display_height = height * sq_size
pattern_file = "data/patterns.json"
colours_file ="data/colours.json"

#Colour settings
colours = tools.load_colours(colours_file)

#TODO so that colours array is not passed multiple times -SC
backgroup_colour = tools.get_colour(colours,"dimgrey")
line_colour = tools.get_colour(colours,"grey")
dead_colour = backgroup_colour
text_colour = tools.get_colour(colours,"lightgrey")
game_over_background_colour = tools.get_colour(colours,"darkgrey")
game_over_text_colour = tools.get_colour(colours,"white")
white = tools.get_colour(colours,"white")

#Text settings
font_size = 40
end_game_font_size = 50

#Loaded from json
patterns = tools.load_patterns(pattern_file)

#TODO Add reset button - JC

def main():
    gui =  Grid_gui()

class Grid_gui:
    def __init__(self):        
        
        pygame.init()

        #Variables which will change during the game
        user_placing_pattern = True
        type = Board_Type['pattern'] 
        self.playing = False
        self.temp_grid = [[False for i in range(height)] for j in range(width)]
        self.screen = pygame.display.set_mode((full_display_width,display_height))
        self.screen.fill(backgroup_colour)
        #default pattern selected
        self.current_pattern = 0
        #default alive colour
        self.current_alive_colour = 0
        self.sq_colour_count = 0
        self.alive_colour = colours[self.sq_colour_count].get_rgb_value()
        #temp blank vars        
        changes = []
        
        #Draws grid
        self.drawGrid() 
        while True:
            self.alive_colour = colours[self.sq_colour_count].get_rgb_value()
            #Draws square to show alive colour
            rect =  pygame.Rect(display_width+30,145,140,sq_size)
            pygame.draw.rect(self.screen,self.alive_colour,rect)

            #Variable so you can differentiate between which screen is currently showing
            game_over = False

            #displays current pattern name 
            pygame.draw.rect(self.screen,backgroup_colour, pygame.Rect(display_width+30,220,230,30))
            font = pygame.font.SysFont(None, font_size)
            pattern_name = patterns[self.current_pattern].get_pattern_name()
            if (len(pattern_name) > 15):
                name_array = [char for char in pattern_name]
                name_array[14] = '.'
                name_array[15] = '.'
                for i in range(16,len(name_array)):
                    name_array.pop()
                str1 = ""
                pattern_name = str1.join(name_array)
            img7 = font.render(pattern_name,True,text_colour) 
            self.screen.blit(img7,(display_width+30,220))

            if self.playing:
                #Wait timer to slow down the game
                pygame.time.wait(1000)
                #Moves the board forward one cycle and saves the changes
                changes = self.board.tick()
                
                
                #If there aren't any changes it then renders a game over screen
                if(len(changes) == 0):
                    #Renders game over screen
                    rect =  pygame.Rect(0,0,full_display_width,display_height)
                    pygame.draw.rect(self.screen,game_over_background_colour,rect)
                    font = pygame.font.SysFont(None, end_game_font_size)
                    game_over_text = font.render('Game over', True, game_over_text_colour)
                    reset = font.render('Reset', True, game_over_text_colour)
                    game_over_rect = game_over_text.get_rect(center=(full_display_width//2, display_height//2))
                    reset_rect = reset.get_rect(center = (full_display_width//2, display_height//1.5))
                    self.screen.blit(game_over_text, game_over_rect)
                    self.screen.blit(reset,reset_rect)
                    game_over = True


            for event in pygame.event.get():

                #Listens for mouse event
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    print(x,y)
                    if not game_over:
                    #If the x cord is within the grid
                        if(x <= display_width):

                            #Works out col and row
                            real_x, real_y = x//sq_size, y//sq_size
                            #Checks if the square is alive
                            if(not self.temp_grid[real_x][real_y]):
                                print("Adding")
                                #If the user has already clicked the pattern button
                                if(user_placing_pattern):
                                    #Places the patten at the x and y the user has just clicked
                                    print("real x y ",real_x,real_y)
                                    self.get_pattern(real_x, real_y)
                            #If it is already alive then it will kill it
                            else:
                                print("Removing")
                                self.temp_grid[real_x][real_y] = False
                                self.draw_sq(real_x*sq_size,real_y*sq_size,dead_colour)


                        #Otherwise the user is placing an individual square
                                
                        #If the mouse event is on the settings panel
                        elif(x > display_width):     
                            #Handles mouse for play
                            if (y >= 20 and y < 60):
                                self.board = Board(width, height, self.temp_grid, type)
                                self.playing = True
                                self.load_sq()     

                            #Handels mouse for random
                            elif ( y >= 60 and y < 100):
                                #Sets type to enum
                                type = Board_Type['random']
                                #Creates a blank grid 
                                grid =""
                                #Creates a board
                                self.board = Board(width, height, grid, type)
                            
                            #If the alive colour button is pressed calls sq_colour
                            elif((y >=130 and y < 170) and (x >= display_width+10 and x <= display_width+25)):
                                print("<")
                                self.sq_colour_count = self.sq_colour_count-1
                                self.set_current_colour()
                                print("back button")
                            
                            elif((y >= 130 and y<170) and (x >= display_width+150 and x <= display_width+190)):
                                print(">")
                                self.sq_colour_count = self.sq_colour_count+1
                                self.set_current_colour()
                    
                                
                            #Mouse events for pattern select
                            elif((y >= 220 and y<=260) and (x >= display_width+10 and x <= display_width+25)):
                                print("<")
                                self.current_pattern = self.current_pattern-1
                                self.set_current_pattern()
                                print("back button")

                            elif((y >= 220 and y<=260) and (x >= display_width+260 and x <= display_width+300)):
                                print(">")
                                self.current_pattern = self.current_pattern+1
                                self.set_current_pattern()
                    else:
                        game_over = False
                        #Variables which will change during the game
                        user_placing_pattern = True
                        self.playing = False
                        self.temp_grid = [[False for i in range(height)] for j in range(width)]
                        self.screen.fill(backgroup_colour)
                        #default pattern selected
                        self.current_pattern = 0
                        #default colour selected
                        self.sq_colour_count = 0
                        self.alive_colour = colours[self.sq_colour_count].get_rgb_value()

                        self.drawGrid() 

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if(debug):
                #Changed for debug
                if(self.playing):
                    self.load_sq()
                else:
                    self.update_by_changes(changes)
            else:
                self.update_by_changes(changes)
            pygame.display.update()

       
    #Draws the grid
    def drawGrid(self):
        for x in range (0,display_width,sq_size):
            for y in range (0,display_height,sq_size):
                rect =  pygame.Rect(x,y,sq_size+1,sq_size+1)
                pygame.draw.rect(self.screen,line_colour,rect,line_size)

        font = pygame.font.SysFont(None, font_size)
        img = font.render('Play', True, text_colour)
        self.screen.blit(img, (display_width+10, 20))

        img2 = font.render('Random', True, text_colour)
        self.screen.blit(img2, (display_width+10, 60))

        img3 = font.render('Cycle Alive Colour', True, text_colour)
        self.screen.blit(img3, (display_width+10, 100))

        img7 = font.render('<',True,text_colour) 
        self.screen.blit(img7,(display_width+10,140))

        img8 = font.render('>',True,text_colour) 
        self.screen.blit(img8,(display_width+180,140))
        
        img4 = font.render('Patterns', True, text_colour)
        self.screen.blit(img4, (display_width+10, 180))

        img5 = font.render('<',True,text_colour) 
        self.screen.blit(img5,(display_width+10,220))

        img6 = font.render('>',True,text_colour) 
        self.screen.blit(img6,(display_width+260,220))
        
    #Loads board onto the grid
    def load_sq(self):
        for x in range(0 ,self.board.get_width()):
            for y in range(0, self.board.get_length()):
                if(self.board.is_sq_alive(x, y)):
                    colour  = self.alive_colour
                else:
                    colour  = dead_colour
                self.draw_sq(x*sq_size,y*sq_size,colour)
                
                if(debug):
                    font = pygame.font.SysFont(None, font_size)
                    img = font.render(str(self.board.neighbours[x][y]), True, tools.get_colour(colours,"black"))
                    self.screen.blit(img, (x*sq_size, y*sq_size))

    #Updates the board based on the changes
    def update_by_changes(self, changes):
        for c in changes:
            x, y, change = c.get_cords()
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
    def set_current_pattern(self):

        if (self.current_pattern > len(patterns)-1) :
            self.current_pattern = 0 
        if (self.current_pattern < 0 ) :
            self.current_pattern = len(patterns)-1
        #print("set pattern test",patterns[self.current_pattern].get_pattern_pattern())

    #Sets current colour
    def set_current_colour(self):

        if (self.sq_colour_count > len(colours)-1) :
            self.sq_colour_count = 0 
        if (self.sq_colour_count < 0 ) :
            self.sq_colour_count = len(colours)-1
        print("set colour test",colours[self.sq_colour_count].get_colour_name())
    
    #Places pattern on the temp grid
    def get_pattern(self, x, y):        
        #Gets currently selected pattern
        #Splits this into char array
        squares = tools.split(patterns[self.current_pattern].get_pattern_pattern())   
        x_pos = 0
        y_pos = 0
        #Loops through this char array
        for c in squares:
            #If the char is a ',' it goes to next line
            if(c == ','):
                y_pos += 1
                x_pos =0
            #If it is a 1 it puts a square and goes to next row
            elif(c == '1'):
                new_x, new_y = x+x_pos, y+y_pos
                #Checks the square will be within the grid
                if(new_x < width and new_y < height):
                    self.temp_grid[new_x][new_y] = True
                    self.draw_sq(new_x*sq_size,new_y*sq_size,self.alive_colour)
                x_pos += 1
            #Otherwise it goes to the next colum
            else:
                x_pos += 1


if __name__ == "__main__":
    main()