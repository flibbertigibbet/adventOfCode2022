#!/usr/bin/env python3

UPPER_OFFSET = 26

priorities = {}
for idx, c in enumerate(map(chr, range(ord("a"), ord("z") + 1)), 1):
    priorities[c] = idx


for idx, c in enumerate(map(chr, range(ord("A"), ord("Z") + 1)), 1):
    priorities[c] = idx + UPPER_OFFSET

with open("data_day3.txt") as data_file:
    data = [x.strip() for x in data_file]
    

##### first puzzle
total_sack_priorities = 0

for sack in data:
    mid = len(sack) // 2
    first = set(sack[:mid])
    second = set(sack[mid:])
    common = first.intersection(second).pop()
    total_sack_priorities += priorities[common]

print(f'total: {total_sack_priorities}')


###### second puzzle
group = []
elf_idx = 0
badge_priorites = 0

for sack in data:
    if elf_idx > 2:
        common = group[0].intersection(group[1]).intersection(group[2]).pop()
        badge_priorites += priorities[common]
        elf_idx = 0
        group = []

    group.append(set(sack))
    elf_idx += 1

# last group
common = group[0].intersection(group[1]).intersection(group[2]).pop()
badge_priorites += priorities[common]

print(f'total badge priorities: {badge_priorites}')
