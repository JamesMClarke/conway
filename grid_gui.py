from random import Random
from boards import Board_Type
from board import Board
import pygame
import sys
import asyncio

#TODO in check neighbours if state is changed pass to list and pass to update   
#TODO 

black =(0,0,0)
white = (255,255,255)
grey = (115, 115, 115)
l_black = (50,50,50)
sq_size = 20
width = 10
height = 10
backgroup_colour = white
line_colour = black
alive_colour = (255, 0, 0)
dead_colour = backgroup_colour
line_size = 1


async def main():
    gui =  Grid_gui()
    #temp blank vars
    """
    Doesn't do anything
    grid =""
    type = Board_Type['random']
    board = Board(10, 10, grid, type)
    gui.drawGrid(board.grid,board.width,board.length)
    while True:
        await asyncio.sleep(1)
        board.tick()
        gui.update_board()
    """

class Grid_gui:

    def __init__(self):        
        
        pygame.init()
        display_width = width * sq_size
        display_height = height * sq_size
        self.screen = pygame.display.set_mode((display_width,display_height))
        self.screen.fill(backgroup_colour)
        #temp blank vars
        grid =""
        type = Board_Type['random']
        board = Board(10, 10, grid, type)
        #TODO Add getters rather than this
        self.grid, self.grid_width, self.grid_length = board.grid, board.width, board.length
        self.drawGrid()
        #move 
        while True:
            #await asyncio.sleep(1)
            board.tick()
            self.update_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

       

    def drawGrid(self):

        self.rect_list = [["" for j in range(self.grid_length)] for i in range(self.grid_width )]
        
        for x in range (0,800,sq_size):
            for y in range (0,800,sq_size):
                rect =  pygame.Rect(x,y,sq_size,sq_size)
                pygame.draw.rect(self.screen,line_colour,rect,line_size)



    #updates square if corropsonding cell depending on state 
    #TODO  change so that it call tick return list of cells whose state has changed in cycle
    #TODO             
    def update_board(self):

        for y in range(0 ,self.grid_length):
            for x in range(0, self.grid_width):
                if(self.grid[x][y].get_is_alive()):
                    self.draw_sq(x*sq_size,y*sq_size,alive_colour)
                else:
                    self.draw_sq(x*sq_size,y*sq_size,dead_colour)

    #draws square 
    def draw_sq(self,x,y,colour):

        rect =  pygame.Rect(x,y,sq_size-line_size,sq_size-line_size)
        pygame.draw.rect(self.screen,colour,rect)


if __name__ == "__main__":
    asyncio.run(main())