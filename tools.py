import json as js
import math
from random import randrange
from sys import implementation
from typing import Coroutine
from pattern import Pattern
from colours import Colour

colours = []


#Tool to load patter from json
def load_patterns(file):
    patterns = []
    try:
        with open(file, "r") as read_file:
            data = js.load(read_file)
            data = data['patterns']
        for x in data:
            patterns.append(Pattern(x['name'], x['pattern'], x['type']))
    except FileNotFoundError:
        patterns.append(Pattern("Error","1","Error"))

    return patterns

#Tool to split word into chars
def split(word):
    return [char for char in word]



def load_colours(file):
    try: 
        with open(file, "r") as read_file:
            data = js.load(read_file)
            data = data['colours']
            for i in data:
                colours.append(Colour(i['colour'],i["rgb_value"]))
                
    except FileNotFoundError:
        colours.append(Colour("Error","1"))
    return colours
    
def get_colour(colour_name):
    for i in range(len(colours)):
        if(colours[i].get_colour_name() == colour_name):
             rgb_value = colours[i].get_rgb_value() 
    return rgb_value 


#TODO implement load and delete custom patterns assigned to -SC
def save_to_json(file, js_obj):

    
        try:
            with open(file,'r+') as file:
                data = js.load(file)
                data['patterns'].append(js_obj)
                file.seek(0)
                js.dump(data,file,indent=4)

        except FileNotFoundError:
            print("error")

def save_custom_pattern(board,name):

    file = "data/patterns.json"
    calculate_furthest_points(board)

    
    

    #removes last , at end of coord string         
    #coord = coord.rstrip(coord[-1])
    #pattern_type = "User"
    #json_obj = {"name":name,"pattern":coord,"type":pattern_type}
    #save_to_json(file,json_obj)


def calculate_furthest_points(board):

    min_x = 0
    max_x = 0

    min_y = 0
    max_y = 0

    coord =""

    #calculates the farthest top,bottom,left,right alive squares
    for i in range(len(board)):
        for j in range (len(board[0])):

            if(board[i][j]==True):

                if ((i < min_x) or (i == 0)):
                    min_x = i
                
                elif(i > max_x):
                    max_x = i

                if ((j < min_y) or (j == 0)):
                    min_y = j

                elif(j > max_y):
                    max_y = j

                
               
              
                


    print("tp ",min_y,"btm ",max_y,"left ",min_x,"right ",max_x)

    y_diff = abs(min_y-max_y)
    x_diff = abs(min_x-max_x)
                
    for i in range (x_diff):
        for j in range (y_diff):

            if(i == x_diff):
                coord += ','
            
            if((board[min_x+i][min_y]==True) or (board[min_x][min_y+j]==True)):
    
                coord += '1'
            

            elif((board[min_x+i][min_y]==False) or (board[min_x][min_y+j]==False)):
                coord += '0'
    
    print(coord)



    #if no pattern to save coord ="" and func returns none

    return







load_colours("data/colours.json")
    
