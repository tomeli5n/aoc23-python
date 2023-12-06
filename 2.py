from pprint import pprint as p
import re

with open('2.input', 'r') as file:
    data = file.readlines()

dictionary= {}

def process_games(data):
    #Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    for line in data:
        sets = re.match(r'Game (\d+): (.*)', line.rstrip('\n'))
        print(sets.groups())
        game = sets.group(1)
        dictionary[game] = []
        for set in sets.group(2).split(";"):
            reveals = set.split(',')
            # ['3 blue', ' 4 red']
            bag = {}
            for reveal in reveals:
                res = re.search(r'(\d+) (\w+)', reveal)
                print("groups ", res.groups())
                color = res.group(2)
                quant = int(res.group(1))
                bag[color] = quant
            dictionary[game].append(bag)

process_games(data)
p(dictionary)
"""
 '3': [{'blue': 6, 'green': 8, 'red': 20},
       {'blue': 5, 'green': 13, 'red': 4},
       {'green': 5, 'red': 1}],
 '4': [{'blue': 6, 'green': 1, 'red': 3},
       {'green': 3, 'red': 6},
       {'blue': 15, 'green': 3, 'red': 14}],
       """

""" TASK 1
Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
"""

