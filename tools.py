import json as js
from pattern import Pattern

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