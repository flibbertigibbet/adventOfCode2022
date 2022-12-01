#!/usr/bin/env python3

with open("data_day1.txt") as data_file:
    data = [x.strip() for x in data_file]
    
total = 0
elves = []

for x in data:
    if x == "":
        elves.append(total)
        total = 0
    else:
        total += int(x)

print(max(elves))


elves.sort()
elves.reverse()
print(sum(sum(elves[:3])))
