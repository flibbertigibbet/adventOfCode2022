#!/usr/bin/env python3

with open("data_day14.txt") as data_file:
    data = [x.strip().split("->") for x in data_file]

ORIGIN_X = 500
ORIGIN_Y = 0

min_x = 10e10
min_y = 0
max_x = 0
max_y = 0

points = [[[int(z) for z in y.strip().split(',')] for y in x] for x in data]

for p in points:
    for x, y in p:
        if x < min_x:
            min_x = x
        
        if x > max_x:
            max_x = x
        
        #if y < min_y:
        #    min_y = y
        
        if y > max_y:
            max_y = y

print(f"min x {min_x} max x {max_x} min y {min_y} max y {max_y}")

cave = [['.'] * (max_x - min_x + 1) for x in range(min_y, max_y + 1)]

def print_cave():
    for c in cave:
        for s in c:
            print(s, end='')
        
        print('')

start_x = None
start_y = None
for p in points:
    start_x, start_y = p[0]
    end_x = None
    end_y = None
    for i in range(1, len(p)):
        if end_x is not None:
            start_x = end_x
            start_y = end_y
        
        end_x, end_y = p[i]

        if start_x == end_x:
            if start_y < end_y:
                for j in range(start_y, end_y+1):
                    cave[j-min_y][start_x-min_x] = '#'
            else:
                for j in range(end_y, start_y+1):
                    print(f'y {j-min_y} x {start_x-min_x}')
                    print(f'cave is {len(cave)} by {len(cave[0])}')
                    cave[j-min_y][start_x-min_x] = '#'
            
        else:
            if start_x < end_x:
                for j in range(start_x, end_x+1):
                    cave[start_y-min_y][j-min_x] = '#'
            else:
                for j in range(end_x, start_x+1):
                    cave[start_y-min_y][j-min_x] = '#'

def settle(from_x, from_y):
    if from_x < min_x or from_x+1 > max_x or from_y < min_y or from_y+1 > max_y:
        print(f'cave is full. {from_x},{from_y}')
        return -1  # cave is full
    
    print(f'settle {from_x},{from_y}')
    if cave[from_y+1-min_y][from_x-min_x] == '.':
        return settle(from_x, from_y+1)
    elif cave[from_y+1-min_y][from_x-1-min_x] == '.':
        return settle(from_x-1, from_y+1)
    elif cave[from_y+1-min_y][from_x+1-min_x] == '.':
        return settle(from_x+1, from_y+1)
    else:
        cave[from_y-min_y][from_x-min_x] = 'o'
        return 0  # rest

print_cave()
grains = 0
full = False
while not full:
    is_full = settle(ORIGIN_X, ORIGIN_Y)
    if is_full == -1:
        full = True
    elif is_full == 0:
        grains += 1

print()
print_cave()
print(f'{grains} grains settled')
