import os
import re

def get_example_input():
    s = """Time:      7  15   30
Distance:  9  40  200"""
    return s.splitlines()

def get_input():
    with open('solutions/day6/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def parse_input(inp):
    times = [int(x) for x in inp[0].split()[1:]]
    distances = [int(x) for x in inp[1].split()[1:]]
    return zip(times, distances)

def task1():
    pairs = parse_input(get_input())
    result = 1
    for time, distance in pairs:
        c = 0
        for acceleration_time in range(1, time):
            run_time = time - acceleration_time
            speed = acceleration_time
            run_distance = run_time * speed
            if run_distance > distance:
                c+=1
        result *= c

    return result

def parse_input_pt2(inp):
    time = int(inp[0].replace(' ', '').split(':')[1])
    distance = int(inp[1].replace(' ', '').split(':')[1])
    return time, distance

def task2():
    time, distance = parse_input_pt2(get_input())
    result = 0
    for acceleration_time in range(1, time):
        run_time = time - acceleration_time
        speed = acceleration_time
        run_distance = run_time * speed
        if run_distance > distance:
            result += 1
    return result