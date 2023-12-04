import os
import math

def get_example_input():
    s = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    return s.splitlines()

def get_input():
    with open('solutions/day4/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def parseline(line):
    card, rest = line.split(': ')
    left, right = rest.split(' | ')
    left_cards = [int(x) for x in left.split(' ') if not x == '']
    right_cards = [int(x) for x in right.split(' ') if not x == '']
    return left_cards, right_cards

def task1():
    result = 0
    for line in get_input():
        left, right = parseline(line)
        union = set(left).intersection(set(right))
        result += int(math.pow(2, len(union) - 1))
    return result

def task2():
    inp = get_input()
    amount = [1 for _ in inp]
    for index, line in enumerate(inp):
        left, right = parseline(line)
        union = set(left).intersection(set(right))
        for i in range(len(union)):
            amount[index + i + 1] += amount[index]
    return sum(amount)