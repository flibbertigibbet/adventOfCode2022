#!/usr/bin/env python3
SIZE = 10

with open("data_day9.txt") as data_file:
    data = [x.strip() for x in data_file]

rows = [0] * SIZE
cols = [0] * SIZE
visited = set()
for x in data:
    dir, dist = x.split(' ')
    dist = int(dist)
    print(f'\n\n{dir} {dist} spaces')
    for i in range(1, dist+1):
        if dir == 'R':
            cols[0] += 1
        elif dir == 'L':
            cols[0] -= 1
        elif dir == 'U':
            rows[0] += 1
        elif dir == 'D':
            rows[0] -= 1
    
        for t in range(1, SIZE):
            if rows[t-1] == rows[t]:
                if cols[t-1] > (cols[t] + 1):
                    cols[t] += 1
                elif cols[t-1] < (cols[t] - 1):
                    cols[t] -= 1
            elif cols[t-1] == cols[t]:
                if rows[t-1] > (rows[t] + 1):
                    rows[t] += 1
                elif rows[t-1] < (rows[t] - 1):
                    rows[t] -= 1
            else: # move diagonally
                if rows[t-1] > (rows[t] + 1):
                    rows[t] += 1
                    if cols[t-1] > cols[t]:
                        cols[t] +=1
                    else:
                        cols[t] -= 1
                elif rows[t-1] < (rows[t] - 1):
                    rows[t] -= 1
                    if cols[t-1] > cols[t]:
                        cols[t] +=1
                    else:
                        cols[t] -= 1
                if cols[t-1] > (cols[t] + 1):
                    cols[t] += 1
                    if rows[t-1] > rows[t]:
                        rows[t] += 1
                    else:
                        rows[t] -= 1
                elif cols[t-1] < (cols[t] - 1):
                    cols[t] -= 1
                    if rows[t-1] > rows[t]:
                        rows[t] += 1
                    else:
                        rows[t] -= 1
    
        visited.add(f'{rows[SIZE-1]}:{cols[SIZE-1]}')
        print(f'move head to {rows[0]}:{cols[0]} tail to {rows[SIZE-1]}:{cols[SIZE-1]}')

print(f'\ntail visited {len(visited)} unique spots')
