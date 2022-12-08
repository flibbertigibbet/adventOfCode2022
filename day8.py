#!/usr/bin/env python3

with open("data_day8.txt") as data_file:
    data = [[int(y) for y in x.strip()] for x in data_file]

visible = (2 * len(data[0])) + (2 * (len(data) - 2))
print(f'got {len(data)} rows and {len(data[0])} columns. {visible} are on exterior')

max_score = 0
for row in range(1, len(data)-1):
    for col in range(1, len(data[0])-1):
        tree = data[row][col]
        print(f'\n\ntree {tree} at {row}:{col}')
        can_see = True
        top_score = 0
        for z in range(row-1, -1, -1): # from top
            top_score += 1
            if tree <= data[z][col]:
                can_see = False
                break
        
        if can_see:
            visible +=1
        
        can_see = True
        bottom_score = 0
        for z in range(row+1, len(data)): # from bottom
            bottom_score += 1
            if tree <= data[z][col]:
                can_see = False
                break

        if can_see:
            visible +=1

        can_see = True
        right_score = 0
        for z in range(col+1, len(data[0])): # from right
            right_score += 1
            if tree <= data[row][z]:
                can_see = False
                break
        
        if can_see:
            visible +=1
        
        can_see = True
        left_score = 0
        for z in range(col-1, -1, -1): # from left
            left_score += 1
            if tree <= data[row][z]:
                can_see = False
                break

        if can_see:
            visible +=1

        score = top_score * bottom_score * left_score * right_score
        if score > max_score:
            max_score = score


print(f'\n\n{visible} total trees are visible')
print(f'max score: {max_score}')
