#!/usr/bin/env python3

with open("data_day8.txt") as data_file:
    data = [[int(y) for y in x.strip()] for x in data_file]

visible = (2 * len(data[0])) + (2 * (len(data) - 2))
print(f'got {len(data)} rows and {len(data[0])} columns. {visible} are on exterior')

for row in range(1, len(data)-1):
    for col in range(1, len(data[0])-1):
        tree = data[row][col]
        print(f'\n\ntree {tree} at {row}:{col}')
        can_see = True
        for z in range(0, row): # from top
            if tree <= data[z][col]:
                can_see = False
                break
        
        if can_see:
            visible +=1
            continue
        
        can_see = True
        for z in range(row+1, len(data)): # from bottom
            if tree <= data[z][col]:
                can_see = False
                break

        if can_see:
            visible +=1
            continue

        can_see = True
        for z in range(col+1, len(data[0])): # from right
            if tree <= data[row][z]:
                can_see = False
                break
        
        if can_see:
            visible +=1
            continue
        
        can_see = True
        for z in range(0, col): # from left
            if tree <= data[row][z]:
                can_see = False
                break

        if can_see:
            visible +=1
            continue


print(f'\n\n{visible} total trees are visible')
