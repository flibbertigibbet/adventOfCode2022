#!/usr/bin/env python3

import ast
from functools import cmp_to_key

with open("data_day13.txt") as data_file:
    data = [x.strip() for x in data_file]

pairs = []
pair = []
for x in data:
    if len(x.strip()) > 0:
        pair.append(x)
    else:
        pairs.append(pair)
        pair = []


in_order = []

def are_in_order(left, right):
    print(f'compare {left} to {right}')
    if type(left) == list and type(right) == list:
        for i in range(len(left)):
            if i > len(right) - 1:
                return -1
            is_in_order = are_in_order(left[i], right[i])
            if is_in_order == 1 or is_in_order == -1:
                return is_in_order
        
        return len(left) < len(right)
    elif type(left) == list or type(right) == list:
        if type(left) == list:
            is_in_order = are_in_order(left, [right])
        else:
            is_in_order = are_in_order([left], right)
        
        return is_in_order
    elif type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    elif left.startswith('[') and right.startswith('['):
        next_left = ast.literal_eval(left)
        next_right = ast.literal_eval(right)
        return are_in_order(next_left, next_right)

    elif left.isnumeric() or right.isnumeric():
        if left.isnumeric():
            is_in_order = are_in_order([left], right)
        else:
            is_in_order = are_in_order(left, [right])
        
        return is_in_order
    
    elif len(left) == 0 or len(right) == 0:
        if len(left) == 0 and len(right) > 0:
            return 1
        elif len(right) == 0 and len(left) > 0:
            return -1
        else:
            return 0
    else:
        print('\nHow did we get here?!')
        print(f"comparing {left} to {right}\n")
        return 0

for idx, pair in enumerate(pairs):
    left, right = pair
    if are_in_order(left, right) == 1:
        in_order.append(idx+1)

print(f"\n\nin-order:\n{in_order}")
print(f"in-order sum: {sum(in_order)}")

# part 2
packets = ["[[2]]", "[[6]]"]
for x in data:
    if len(x.strip()) > 0:
        packets.append(x)

packets.sort(key=cmp_to_key(are_in_order), reverse=True)

FIRST_DISTRESS = "[[2]]"
SECOND_DISTRESS = "[[6]]"

first_packet = -1
second_packet = -1
for idx, packet in enumerate(packets):
    if packet == FIRST_DISTRESS:
        first_packet = idx + 1
    elif packet == SECOND_DISTRESS:
        second_packet = idx + 1
    
    if first_packet > 0 and second_packet > 0:
        break

print(f"Found {first_packet} and {second_packet} indices")
print(f"Multiple is {first_packet * second_packet}")
