#!/usr/bin/env python3

with open("data_day6.txt") as data_file:
    data = [x.strip() for x in data_file]

data = data[0]

SIZE = 14

for x in range(SIZE, len(data)):
    if (len(set(data[x-SIZE:x])) == SIZE):
        print(f"Unique set {data[x-SIZE:x]} found at {x}")
        break
    
print(f'done')
