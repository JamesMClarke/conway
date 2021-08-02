import json as js
from pattern import Pattern
from colours import Colour

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
    colours = []
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
def get_colour(colours,colour_name):
    for i in range(len(colours)):
         if(colours[i].get_colour_name() == colour_name):
             rgb_value = colours[i].get_rgb_value() 
    return rgb_value 



load_colours("data/colours.json")
    
