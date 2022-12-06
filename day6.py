#!/usr/bin/env python3

with open("data_day6.txt") as data_file:
    data = [x.strip() for x in data_file]

data = data[0]

for x in range(3, len(data)):
    if (len(set(data[x-4:x])) == 4):
        print(f"Unique set {data[x-4:x]} found at {x}")
        break
    
print(f'done')
