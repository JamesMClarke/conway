import json as js
from random import randrange
from sys import implementation
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
    
#TODO remove this once colour is redone
def get_colour(colour_name):
    for i in range(len(colours)):
        if(colours[i].get_colour_name() == colour_name):
             rgb_value = colours[i].get_rgb_value() 
    return rgb_value 

def save_custom_pattern(board):

    final_coord =""

    for j in range (40):
        for i in range(70):
            if(board[i][j]== True):
                x = f'{i:08b}'
                y = f'{j:08b}'
                print("x y = ",x,y)
                coord = x,y
                
                final_coord += str(coord)

                #coords = str()
    type = "custom"
    name = "test"
    custom = Pattern(name,final_coord,type)
    print(custom.get_pattern_name(),"  ",custom.get_pattern_pattern()," ",custom.get_pattern_type())




load_colours("data/colours.json")
    
