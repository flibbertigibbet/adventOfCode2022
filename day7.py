#!/usr/bin/env python3

MAX_SIZE = 100000
TOTAL_SPACE = 70000000
NEED_SPACE = 30000000

with open("data_day7.txt") as data_file:
    data = [x.strip() for x in data_file]

curdir = ''
curparent = ''
dirs = {}
for x in data:
    if x.startswith('$'):
        cmd = x.split(' ')
        if cmd[1] == 'cd':
            if cmd[2] == '..':
                curdir = curparent
                curparent = dirs[curparent]['parent']
            else:
                curparent = curdir
                curdir = curdir + '/' + cmd[2] if len(curdir) > 0 else cmd[2]
        else: # ls
            dirs[curdir] = {
                'size': 0,
                'children': [],
                'parent': curparent
            }
    elif x.startswith('dir'):
        dirs[curdir]['children'].append(x.split(' ')[1])
    else:
        dirs[curdir]['size'] += int(x.split(' ')[0])

# print(f"got dirs {dirs}")

def sum_dir_size(dir):
    size = dirs[dir]['size']
    for child in dirs[dir]['children']:
        size += sum_dir_size(dir + '/' + child)
    
    return size

total_dir_size = 0
for d in dirs:
    dirsize = sum_dir_size(d)
    if dirsize <= MAX_SIZE:
        total_dir_size += dirsize

print(f'\n\ntotal matching directory size: {total_dir_size}')

# part 2
empty = TOTAL_SPACE - sum_dir_size('/')
need = NEED_SPACE - empty

smallest = TOTAL_SPACE
for d in dirs:
    dirsize = sum_dir_size(d)
    if dirsize >= need and dirsize < smallest:
        smallest = dirsize

print(f"\n\nSmallest directory with {need} space free is {smallest}")
