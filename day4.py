#!/usr/bin/env python3

with open("data_day4.txt") as data_file:
    data = [x.strip() for x in data_file]
    
# print(f"got data: {data}")

contained = 0
for x in data:
    elf1, elf2 = x.split(',')
    elf1min, elf1max = elf1.split('-')
    elf2min, elf2max = elf2.split('-')
    if int(elf1min) <= int(elf2min) and int(elf1max) >= int(elf2max):
        contained += 1
    elif int(elf2min) <= int(elf1min) and int(elf2max) >= int(elf1max):
        contained += 1

print(f"{contained} out of {len(data)} elf pairs fully overlap")
