import os
from functools import reduce
try:
    from tqdm import tqdm
except:
    def tqdm(l): return l

import concurrent.futures

def get_example_input():
    s = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    return s.splitlines()

def get_input():
    with open('solutions/day5/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def parse_input(inp, range_mode=False):
    seeds = []
    maps = []
    for line in inp:
        if line.startswith('seeds:'):
            seeds = [int(x) for x in line.split(': ')[1].split(' ')]
            if range_mode:
                starts = [x for x in seeds[0::2]]
                ranges = [x for x in seeds[1::2]]
                seeds = [range(x, x+y) for x, y in zip(starts, ranges)]
        elif line == '':
            maps.append([])
        elif not line[0].isdigit():
            continue
        else:
            destination, source, _range = [int(x) for x in line.split(' ')]
            maps[-1].append((range(source, source+_range), range(destination, destination+_range)))
    return seeds, maps

def task1():
    seeds, table = parse_input(get_input())
    results = []
    # print(seeds)
    for seed in tqdm(seeds):
        # print(f'Seed: {seed}')
        for translation in table:
            # print('---- Translation Step ---')
            for line in translation:
                if seed in line[0]:
                    index = line[0].index(seed)
                    # print(f'Found translation: {seed} -> {line[0]} -> {line[1]}')
                    seed = line[1][index]
                    # print(f'New number: {seed}')
                    break
        results.append(seed)
    return min(results)

def do_seed(seed, table):
    for translation in table:
        # print('---- Translation Step ---')
        for line in translation:
            if seed in line[0]:
                index = line[0].index(seed)
                # print(f'Found translation: {seed} -> {line[0]} -> {line[1]}')
                seed = line[1][index]
                # print(f'New number: {seed}')
                break
    return seed


def task2():
    seeds, table = parse_input(get_input(), True)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for seed in seeds:
            for elem in seed:
                # print(f'Starting thread for seed: {elem}')
                futures.append(executor.submit(do_seed, seed=elem, table=table))
        print(f'Starting to collect threads')
        for future in concurrent.futures.as_completed(futures):
            print(f'.')
            results.append(future.result())    
    return min(results)
    '''
    possible_locations = range(0, 3015666186+477873382)
    results = []
    for starter in tqdm(possible_locations):
        current = starter
        for translation in reversed(table):
            for line in translation:
                if current in line[1]:
                    index = line[1].index(current)
                    current = line[0][index]
                    break
        results.append(current)
    valids = []
    for result in results:
        for seedrange in seeds:
            if result in seedrange:
                valids.append(result)
                break
    results = []
    for seed in tqdm(valids):
        for translation in table:
            for line in translation:
                if seed in line[0]:
                    index = line[0].index(seed)
                    seed = line[1][index]
                    break
        results.append(seed)
    return min(results)
    '''