#!/usr/bin/env python3

import itertools

SIDES = 6

with open("data_day18test.txt") as data_file:
    data = [x.strip().split(',') for x in data_file]
    data = [(int(x[0]), int(x[1]), int(x[2])) for x in data]

matched = 0
touching = 0
for one, two in itertools.pairwise(data):
    if (one[0] == two[0] and one[1] == two[1]) or (
        one[1] == two[1] and one[2] == two[2]) or (
        one[2] == two[2] and one[0] == two[0]):
        #touching += 2
        diff_sum = sum([abs(x - y) for x, y in zip(one, two)])
        if diff_sum <= 2:
            print(f'{one} and {two} are touching')
            touching += 2

print(f'{touching} sides are touching from {len(data)} cubes')
surface = (SIDES * len(data)) - touching
print(f'\n\n{surface} surface area')
