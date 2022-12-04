#!/usr/bin/env python3

with open("data_day4.txt") as data_file:
    data = [x.strip() for x in data_file]

contained = 0
partial = 0
for x in data:
    elf1, elf2 = x.split(',')
    elf1min, elf1max = [int(x) for x in elf1.split('-')]
    elf2min, elf2max = [int(x) for x in elf2.split('-')]

    # part 1
    if elf1min <= elf2min and elf1max >= elf2max:
        contained += 1
    elif elf2min <= elf1min and elf2max >= elf1max:
        contained += 1

    # part 2
    if (elf1min <= elf2max and elf1max >= elf2max) or (elf2min <= elf1max and elf2max >= elf1max):
        partial += 1

print(f"{contained} out of {len(data)} elf pairs fully overlap")
print(f"{partial} elf pairs partially overlap")
