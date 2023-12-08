import os
from itertools import cycle
import re
from math import lcm

def get_example_input():
    s = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
    s = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
    
    return s.splitlines()

def get_input():
    with open('solutions/day8/input.txt') as f:
        return [x.strip() for x in f.readlines()]

LINE_PATTERN = re.compile(r'(?P<from>\w+)\s=\s\((?P<toleft>\w+),\s(?P<toright>\w+)\)')

def parse_input(inp):
    steps = cycle([int(x) for x in inp[0].replace('L', '0').replace('R', '1')])
    guides = {}
    for line in inp[2:]:
        if match := LINE_PATTERN.match(line):
            _from, left, right = match.groups()
            guides[_from] = (left, right)
    return steps, guides

def task1():
    steps, guides = parse_input(get_input())
    current = 'AAA'
    steps_walked = 0
    while not current == 'ZZZ':
        options = guides[current]
        current = options[next(steps)]
        steps_walked += 1
    return steps_walked

def get_example_input_pt2():
    s = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    return s.splitlines()
    

def find_starts(guides):
    return [x for x in guides.keys() if x.endswith('A')]

def task2():
    steps, guides = parse_input(get_input())
    current = find_starts(guides)
    steps_walked = 0
    found_Zs = []
    while len(found_Zs) < len(current):
        n = next(steps)
        for index, elem in enumerate(current):
            options = guides[elem]
            current[index] = options[n]
            if current[index].endswith("Z"):
                found_Zs.append(steps_walked + 1)
        steps_walked += 1
    return lcm(*found_Zs)