#!/usr/bin/env python3

with open("data_day10.txt") as data_file:
    data = [x.strip() for x in data_file]

cycles = [x for x in range(20, 260, 40)]

xreg = 1
cycle = 1
signal_sum = 0
for x in data:
    if x.startswith('addx'):
        if (cycle + 1) in cycles:
            print(f'adding off cycle {cycle + 1} amt {(cycle + 1) * xreg}')
            signal_sum += (cycle + 1) * xreg
        cycle += 2
        _, amt = x.split(' ')
        xreg += int(amt)
    else:
        cycle += 1
    
    if cycle in cycles:
        print(f'adding cycle {cycle} amt {cycle * xreg}')
        signal_sum += cycle * xreg

print(f'signal sum: {signal_sum}')
