import json as js
from random import randrange
from sys import implementation
from typing import Coroutine
from pattern import Pattern
from colours import Colour

colours = []
old_sq_x = 0
old_sq_y = 0
top_alive_sq = 0
bottom_alive_sq = 0
left_alive_sq = 0
right_alive_sq = 0

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

    global old_sq_x
    global old_sq_y
    global top_alive_sq
    global bottom_alive_sq
    global left_alive_sq
    global right_alive_sq

    #calculates the farthest top,bottom,left,right alive squares
    #TODO Bug save has to be ran twice for the top and bottm alive squares to print correctly ? -SC
    #TODO flaw in logic 
    for i in range(len(board)):
        for j in range (len(board[0])):

            if(board[i][j]==True):
                current_sq_x = i 
                current_sq_y = j
                
                #Finds the furthest top and bottom alive squares
                if ((current_sq_y <= old_sq_y)and (current_sq_x, current_sq_y != top_alive_sq)):
                    
                    top_alive_sq = None
                    old_sq_y = current_sq_y
                    old_sq_x = current_sq_x
                    top_alive_sq = old_sq_x,old_sq_y

                if((current_sq_y >= old_sq_y) and (current_sq_x, current_sq_y != bottom_alive_sq)):

                    bottom_alive_sq = None
                    old_sq_y = current_sq_y
                    old_sq_x = current_sq_x
                    bottom_alive_sq = old_sq_x,old_sq_y   

                #finds farthest left and right alive squares
               

                if((current_sq_x <= old_sq_x) and (current_sq_x, current_sq_y != left_alive_sq)):

                    left_alive_sq = None
                    old_sq_y = current_sq_y
                    old_sq_x = current_sq_x
                    left_alive_sq = old_sq_x,old_sq_y   

                if((current_sq_x >= old_sq_x) and (current_sq_x, current_sq_y != right_alive_sq)):
                            
                    right_alive_sq = None
                    old_sq_y = current_sq_y
                    old_sq_x = current_sq_x
                    right_alive_sq = old_sq_x,old_sq_y


    print(top_alive_sq,bottom_alive_sq,left_alive_sq,right_alive_sq)





                #Works out the most left alive square and most right square
                
           #for j in range (width_distance):
#               for i in range (height_distance):

 #                  if(j == width_dist):
                       #add , to end of coord
                   
  #                 if (board[left_alive+i][top_alive+j]==True):
                       # if  j == width_dist add , to end of string
   #                    pass
    #               if (board[left_alive+i][top_alive+j]==False):
     #                  pass
    




    #if no pattern to save coord ="" and func returns none
    

    #removes last , at end of coord string         
    #coord = coord.rstrip(coord[-1])
    #pattern_type = "User"
    #json_obj = {"name":name,"pattern":coord,"type":pattern_type}
    #save_to_json(file,json_obj)


    







load_colours("data/colours.json")
    
