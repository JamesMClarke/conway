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

def save_custom_pattern(board,name, file):
    
    min_x, max_x, min_y, max_y = 0,0,0,0

    coord = ''

    #calculates the farthest top,bottom,left,right alive squares
    for i in range(len(board)):
        for j in range (len(board[0])):

            if(board[i][j]==True):

                if ((i < min_x) or (min_x == 0)):
                    min_x = i
                
                if(i > max_x):
                    max_x = i

                if ((j < min_y) or (min_y == 0)):
                    min_y = j

                if(j > max_y):
                    max_y = j


    print("tp ",min_y,"btm ",max_y,"left ",min_x,"right ",max_x)
                
    
    for j in range (min_y, max_y+1):
        for i in range (min_x, max_x+1):
            if(board[i][j]==True):
                coord += '1'
            else:
                coord += '0'

        coord += ','
    
    


    

    #removes last , at end of coord string         
    coord = coord.rstrip(coord[-1])
    print(coord)
    pattern_type = "User"
    json_obj = {"name":name,"pattern":coord,"type":pattern_type}
    save_to_json(file,json_obj)
    
    return
#pass custom patttern name
def delete_pattern(name):
    #if type = User
    file = 'data/patterns.json'
    pattern_name = name

    try:
        with open(file,'r+') as file:
            data = js.load(file)
            pattern_data = data['patterns']
            for i in range (len(pattern_data)):
                
                if(pattern_data[i]['name'] == pattern_name):
                    if(pattern_data[i]['type'] == "User"):
                        print(pattern_data[i]['type'])

                        
                        file.seek(0)
                        pattern_data.pop(i)              
                        file.truncate(0)
                        js.dump(data,file,indent=4)
                        break
                    elif(not pattern_data[i]['type'] == 'User'):
                        print('Protected pattern')
                        break
                    

        
    


                

                   
    except FileNotFoundError:

        print("error")






load_colours("data/colours.json")
