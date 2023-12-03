import os

def get_example_input():
    s = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    return s.splitlines()

def get_input():
    with open('solutions/day3/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def adjacent_coordinates(x, y):
    return [
        (x - 1, y),
        (x - 1, y - 1),
        (x , y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
    ]

def check_adjacent(x, y, _map):
    for coordinate in adjacent_coordinates(x, y):
        if _map[coordinate[0]][coordinate[1]] != '.' and not _map[coordinate[0]][coordinate[1]].isdigit():
            return True
    return False

def prepare_map(_map: list):
    for index, line in enumerate(_map):
        _map[index] = f'.{line}.'
    _map.insert(0, ''.join(['.' for _ in range(len(_map[0]))]))
    _map.append(''.join(['.' for _ in range(len(_map[0]))]))
    for line in _map:
        assert len(line) == len(_map[0])
    return _map

def task1():
    prepared_map = prepare_map(get_input())
    valid_numbers = []
    current_numbers = []
    current_valid = False
    for x, line in enumerate(prepared_map):
        for y, char in enumerate(line):
            if char.isdigit():
                if not current_valid:
                    current_valid = check_adjacent(x, y, prepared_map)
                current_numbers.append(char)
            else:
                if current_valid:
                    valid_numbers.append(int(''.join(current_numbers)))
                current_valid = False
                current_numbers = []
    return sum(valid_numbers)

def task2():
    return ''