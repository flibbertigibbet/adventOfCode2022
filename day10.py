#!/usr/bin/env python3

with open("data_day10.txt") as data_file:
    data = [x.strip() for x in data_file]

cycles = [x for x in range(20, 260, 40)]

# part 2
WIDTH = 40

def draw(cycle, xreg):
    pixel = cycle - 1 - ((cycle // WIDTH) * WIDTH)
    if xreg >= pixel - 1 and xreg <= pixel + 1:
        print('#', end='')
    else:
        print('.', end='')
    
    if cycle % WIDTH == 0:
        print('')

xreg = 1
cycle = 1
signal_sum = 0
draw(cycle, xreg)
for x in data:
    if x.startswith('addx'):
        cycle += 1
        if cycle in cycles:
            signal_sum += cycle * xreg
        
        draw(cycle, xreg)
        cycle += 1
        _, amt = x.split(' ')
        xreg += int(amt)
        draw(cycle, xreg)
    else:
        cycle += 1
        draw(cycle, xreg)
    
    if cycle in cycles:
        signal_sum += cycle * xreg

print(f'\n\nsignal sum: {signal_sum} last cycle was {cycle}')
