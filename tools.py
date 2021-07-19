import json as js
from pattern import Pattern

#Tool to load patter from json
def load_patterns():
    patterns = []
    with open("patterns.json", "r") as read_file:
        data = js.load(read_file)
        data = data['patterns']
    for x in data:
        patterns.append(Pattern(x['name'], x['pattern'], x['type']))
    return patterns

#Tool to split word into chars
def split(word):
    return [char for char in word]