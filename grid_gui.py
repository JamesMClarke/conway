from board import Board
from cords import Cords
from random import getrandbits
import tools
import pygame
import sys

#TODO Allow user to save custom patterns into json - JC
#TODO Add something that shows the user details about the pattern -JC
#E.G. If it is a user pattern, or still life

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

backgroup_colour = tools.get_colour("dimgrey")
line_colour = tools.get_colour("grey")
dead_colour = backgroup_colour
text_colour = tools.get_colour("lightgrey")
game_over_background_colour = tools.get_colour("darkgrey")
game_over_text_colour = tools.get_colour("white")
white = tools.get_colour("white")

#Text settings
font_size = 40
end_game_font_size = 50

#Loaded from json
patterns = tools.load_patterns(pattern_file)

def main():
    gui =  Grid_gui()

class Grid_gui:
    def __init__(self):        
        
        pygame.init()

        #Variables which will change during the game
        user_placing_pattern = True
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

        #Variable so you can differentiate between which screen is currently showing
        self.game_over = False

        #Draws grid
        self.drawGrid() 
        while True:
            #Draws square to show alive colour
            rect =  pygame.Rect(display_width+30,145,140,sq_size)
            pygame.draw.rect(self.screen,self.alive_colour,rect)
            
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


            #Shows the pattern type
            pygame.draw.rect(self.screen,backgroup_colour, pygame.Rect(display_width+90,260,230,30))
            pattern = font.render(patterns[self.current_pattern].get_pattern_type(), True, text_colour)
            self.screen.blit(pattern,(display_width+90, 260))

            if self.playing:
                print(self.game_over)
                if(not self.game_over):
                    #Wait timer to slow down the game
                    pygame.time.wait(1000)
                    #Moves the board forward one cycle and saves the changes
                    changes = self.board.tick()
                
                
                #If there aren't any changes it then renders a game over screen
                if(len(changes) == 0):
                    self.game_over = True
                    #Renders game over screen
                    rect =  pygame.Rect(0,0,full_display_width,display_height)
                    pygame.draw.rect(self.screen,game_over_background_colour,rect)
                    font = pygame.font.SysFont(None, end_game_font_size)
                    game_over_text = font.render('Game over', True, game_over_text_colour)
                    reset = font.render('Reset', True, game_over_text_colour)
                    quit = font.render('Quit', True, game_over_text_colour)
                    game_over_rect = game_over_text.get_rect(center=(full_display_width//2, display_height//2))
                    reset_rect = reset.get_rect(center = (full_display_width//4, display_height//1.5))
                    quit_rect = reset.get_rect(center =((full_display_width//4)*3, display_height//1.5))
                    self.screen.blit(game_over_text, game_over_rect)
                    self.screen.blit(reset,reset_rect)
                    self.screen.blit(quit, quit_rect)
                    


            for event in pygame.event.get():

                #Listens for mouse event
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    print(x,y)
                    if not self.game_over:
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

                                self.board = Board(width, height, self.temp_grid)
                                self.playing = True
                                self.load_sq()     

                            #Handels mouse for random
                            elif ( y >= 60 and y < 100):
                                self.temp_grid = [[(bool(getrandbits(1))) for j in range(height)] for i in range(width)]
                                self.load_temp()
                            
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
                            
                            #Mouse events for reset
                            elif((y >= 300 and y<340) and (x >= display_width+10 and x <= display_width+200)):
                                self.game_over = True
                                self.reset_board()

                            #Mouse event for save board
                            elif((y >= 340 and y<=380) and (x >= display_width+10 and x <= display_width+200)):
                                tools.save_custom_pattern(self.temp_grid,height,width)

                            #Mouse event to quit game
                            elif((y >= 380 and y<=420) and (x >= display_width+10 and x <= display_width+200)):
                                pygame.quit()
                                sys.exit()
                            


                    else:
                        if(x < full_display_width//2):
                            self.game_over = True
                            self.reset_board()
                        else:
                            pygame.quit()
                            sys.exit()

                        

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

    def reset_board(self):

        self.game_over = False
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
       
    #Draws the grid
    def drawGrid(self):
        for x in range (0,display_width,sq_size):
            for y in range (0,display_height,sq_size):
                rect =  pygame.Rect(x,y,sq_size+1,sq_size+1)
                pygame.draw.rect(self.screen,line_colour,rect,line_size)

        font = pygame.font.SysFont(None, font_size)

        self.screen.blit(font.render('Play', True, text_colour), (display_width+10, 20))

        self.screen.blit(font.render('Random', True, text_colour), (display_width+10, 60))

        self.screen.blit(font.render('Cycle Alive Colour', True, text_colour), (display_width+10, 100))

        self.screen.blit(font.render('<',True,text_colour),(display_width+10,140))

        self.screen.blit(font.render('>',True,text_colour),(display_width+180,140))
        
        self.screen.blit(font.render('Pattern:', True, text_colour), (display_width+10, 180))

        self.screen.blit(font.render('<',True,text_colour) ,(display_width+10,220))

        self.screen.blit(font.render('>',True,text_colour) ,(display_width+260,220))

        self.screen.blit(font.render('Type:', True, text_colour), (display_width+10, 260))

        self.screen.blit(font.render("Reset Board",True,text_colour),(display_width+10,300))

        self.screen.blit(font.render("save pattern",True,text_colour),(display_width+10,340))

        self.screen.blit(font.render("Quit game",True,text_colour),(display_width+10,380))

        
    #Loads board onto the grid
    def load_sq(self):
        for x in range(0 ,self.board.get_width()):
            for y in range(0, self.board.get_height()):
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

    def load_temp(self):
        for x in range(0 ,len(self.temp_grid)):
            for y in range(0, len(self.temp_grid[0])):
                if(self.temp_grid[x][y]):
                    colour  = self.alive_colour
                else:
                    colour  = dead_colour
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

        self.alive_colour = colours[self.sq_colour_count].get_rgb_value()
        self.load_temp()
    
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