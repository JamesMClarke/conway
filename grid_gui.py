from random import Random
from functools import partial
import random
from boards import Board_Type
import pygame
import sys

#TODO in check neighbours if state is changed pass to list and pass to update   

black =(0,0,0)
white = (255,255,255)
grey = (115, 115, 115)
l_black = (50,50,50)
rectSize = 10
display_width = 800
display_height = 800


class Grid_gui:


    def __init__(self):        
        

        pygame.init()
        self.screen = pygame.display.set_mode((display_width,display_height))
        self.screen.fill(black)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

       

        #self.window_width = str(self.grid_width *self.rect_size)
        #self.window_height = str(self.grid_length *self.rect_size)
        #self.window_size = (self.window_width+'x'+self.window_height)  
        #print('window size =',self.window_size)

    def drawGrid(self,grid,grid_width,grid_length):

        self.grid = grid
        self.grid_width = grid_width
        self.grid_length = grid_length
        self.rect_list = [["" for j in range(self.grid_length)] for i in range(self.grid_width )]
        
        for x in range (0,800,rectSize):
            for y in range (0,800,rectSize):
                rect =  pygame.Rect(x,y,rectSize,rectSize)
                pygame.draw.rect(self.screen,white,rect,1)
              
               
    def update_board(self):

        for y in range(0 ,self.grid_length):
            for x in range(0, self.grid_width ):
                if(self.grid[x][y].get_is_alive()):
                    self.draw_sq(x,y,grey)
                else:
                    self.draw_sq(x,y,l_black)


    def draw_sq(self,x,y,colour):

        rect =  pygame.Rect(x,y,rectSize,rectSize)
        pygame.draw.rect(self.screen,colour,rect)

    def get_grid(self):
        type = Board_Type['random']
        grid =""
        return grid,type

    def get_width(self):
        width = display_width
        return width

    def get_height(self):
        height = display_height
        return height