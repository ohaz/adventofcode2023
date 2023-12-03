import os
import math

def get_example_input():
    s = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    return s.splitlines()

def get_input():
    with open('solutions/day2/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def splitline(line):
    game, takes = line.split(': ')
    game = int(game.split(' ')[1])
    takes = takes.split('; ')
    t = []
    for take in takes:
        t.append({})
        for entry in take.split(', '):
            t[-1][entry.split(' ')[-1]] = int(entry.split(' ')[0])
    return game, t

def task1():
    maxcubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    games_possible = []
    for line in get_input():
        split = splitline(line)
        valid = True
        for entry in split[1]:
            for key, value in entry.items():
                if maxcubes[key] < value:
                    valid = False
        if valid:
            games_possible.append(split[0])
        
    return sum(games_possible)

def task2():
    powers = []
    for line in get_input():
        maxs = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        split = splitline(line)
        for entry in split[1]:
            for key, value in entry.items():
                maxs[key] = max(maxs[key], value)
        powers.append(math.prod(maxs.values()))

    return sum(powers)