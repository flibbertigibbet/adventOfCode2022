#!/usr/bin/env python3

with open("data_day5.txt") as data_file:
    data = [x for x in data_file]

stack_rows = []
moves = []
for x in data:
    if "move" in x:
        words = x.strip('\n').split(' ')
        moves.append([int(words[1]), int(words[3]), int(words[5])])
    else:
        row = [ y.strip('\n').strip('[').strip(']') for y in x.replace('    ', ' ').split(' ')]
        if len(row) > 1:
            stack_rows.append(row)

stack_rows.pop() # label row
stack_rows.reverse()

stacks = [[] for x in range(len(stack_rows[0]))]
for row in stack_rows:
    for idx, val in enumerate(row):
        if len(val) > 0:
            stacks[idx].append(val)

for amt, from_s, to_s in moves:
    print(stacks[from_s-1])
    print(stacks[to_s-1])
    for _ in range(amt):
        c = stacks[from_s-1].pop()
        stacks[to_s-1].append(c)

final_message = ''.join([s.pop() for s in stacks])
print(final_message)
