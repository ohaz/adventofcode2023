import os

def get_example_input():
    s = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    return s.splitlines()

def get_example_input_2():
    s = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    return s.splitlines()

def get_input():
    with open('solutions/day1/input.txt') as f:
        return [x.strip() for x in f.readlines() if not x.strip() == '']

def task1():
    # inp = get_example_input()
    inp = get_input()
    filtered = [list(filter(lambda x: x.isdigit(), l)) for l in inp]
    numbers = [int(x[0] + x[-1]) for x in filtered]
    return sum(numbers)

def task2():
    mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    # inp = get_example_input_2()
    inp = get_input()
    items = []
    for line in inp:
        nums = []
        for index in range(1, len(line)+1):
            slice = line[:index]
            if slice[-1].isdigit():
                nums.append(slice[-1])
            for key, value in mapping.items():
                if slice.endswith(key):
                    nums.append(value)
        items.append(int(nums[0] + nums[-1]))
    return sum(items)