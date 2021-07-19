import json as js
from pattern import Pattern

def load_patterns():
    patterns = []
    with open("patterns.json", "r") as read_file:
        data = js.load(read_file)
        data = data['patterns']
    for x in data:
        patterns.append(Pattern(x['name'], x['pattern'], x['type']))
    return patterns

patterns = load_patterns()

def get_patterns():
    return patterns