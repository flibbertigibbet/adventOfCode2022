#!/usr/bin/env python3

import ast

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
                print(f"right list {right} is shorter than {left}; NOT in order")
                return -1
            is_in_order = are_in_order(left[i], right[i])
            if is_in_order == 1 or is_in_order == -1:
                print(f'recursively found for lists {left} and {right} in order? {is_in_order}')
                return is_in_order
        
        return len(left) < len(right)
    elif type(left) == list or type(right) == list:
        if type(left) == list:
            is_in_order = are_in_order(left, [right])
        else:
            is_in_order = are_in_order([left], right)
        
        return is_in_order
    elif type(left) == int and type(right) == int:
        print(f'compare one int and one not: {left} to {right}')
        if left < right:
            print(f"ints {left} and {right} are in order")
            return 1
        elif left == right:
            print(f"ints {left} and {right} are the same")
            return 0
        else:
            print(f"ints {left} and {right} are NOT in order")
            return -1

    elif left.startswith('[') and right.startswith('['):
        next_left = ast.literal_eval(left)
        next_right = ast.literal_eval(right)
        print(f'parse and compare {next_left} to {next_right}')
        return are_in_order(next_left, next_right)

    elif left.isnumeric() or right.isnumeric():
        print('How did we get here for numeric comp?')
        if left.isnumeric():
            is_in_order = are_in_order([left], right)
        else:
            is_in_order = are_in_order(left, [right])
        
        return is_in_order
    
    elif len(left) == 0 or len(right) == 0:
        if len(left) == 0 and len(right) > 0:
            print('left is empty so in order')
            return 1
        elif len(right) == 0 and len(left) > 0:
            print('right is empty so NOT  in order')
            return -1
        else:
            print('both empty?!?!?')
            return 0
    else:
        print('\nHow did we get here?!')
        print(f"comparing {left} to {right}\n")
        return 0

for idx, pair in enumerate(pairs):
    left, right = pair
    print(f'\nchecking pair {idx+1}')
    if are_in_order(left, right) == 1:
        in_order.append(idx+1)

print(f"\n\nin-order:\n{in_order}")
print(f"in-order sum: {sum(in_order)}")