#!/usr/bin/env python3

with open("data_day9.txt") as data_file:
    data = [x.strip() for x in data_file]

hrow = 0
hcol = 0
trow = 0
tcol = 0
visited = set()
for x in data:
    dir, dist = x.split(' ')
    dist = int(dist)
    print(f'\n\n{dir} {dist} spaces')
    for i in range(1, dist+1):
        if dir == 'R':
            hcol += 1
        elif dir == 'L':
            hcol -= 1
        elif dir == 'U':
            hrow += 1
        elif dir == 'D':
            hrow -= 1
    
        if hrow == trow:
            if hcol > (tcol + 1):
                tcol += 1
            elif hcol < (tcol - 1):
                tcol -= 1
        elif hcol == tcol:
            if hrow > (trow + 1):
                trow += 1
            elif hrow < (trow - 1):
                trow -= 1
        else: # move diagonally
            if hrow > (trow + 1):
                trow += 1
                if hcol > tcol:
                    tcol +=1
                else:
                    tcol -= 1
            elif hrow < (trow - 1):
                trow -= 1
                if hcol > tcol:
                    tcol +=1
                else:
                    tcol -= 1
            if hcol > (tcol + 1):
                tcol += 1
                if hrow > trow:
                    trow += 1
                else:
                    trow -= 1
            elif hcol < (tcol - 1):
                tcol -= 1
                if hrow > trow:
                    trow += 1
                else:
                    trow -= 1
    
        visited.add(f'{trow}:{tcol}')
        print(f'move head to {hrow}:{hcol} tail to {trow}:{tcol}')

print(f'\ntail visited {len(visited)} unique spots')
