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

def save_custom_pattern(board,height,width):

    file = "data/patterns.json"
    coord =""
    #TODO aloow user to name patterns assigned to -SC
    for j in range (height):
        for i in range(width):
            
            #converts alive squares coords on board to binary adds to coord string
            if(board[i][j]== True):
                x = f'{i:08b}'
                y = f'{j:08b}'
                print("x y = ",x,y)
                coord += x+','
                coord += y+',' 

    #if no pattern to save coord ="" and func returns none
    if(coord ==""):
        return

    #removes last , at end of coord string         
    coord = coord.rstrip(coord[-1])
    print("coord=", coord)
    pattern_type = "User"
    name = "Custom pattern"
    json_obj = {"name":name,"pattern":coord,"type":pattern_type}
    save_to_json(file,json_obj)


    







load_colours("data/colours.json")
    
