#!/usr/bin/env python3

with open("data_day11.txt") as data_file:
    data = [x.strip() for x in data_file]

ROUNDS = 10000
monkeys = []
monkey = None
for x in data:
    if x.startswith('Monkey'):
        if monkey:
            monkeys.append(monkey)
        
        monkey = {'total_inspections': 0}
    elif x.startswith('Starting items'):
        monkey['items'] = [int(i.strip()) for i in x.split(':')[1].strip().split(',')]
    elif x.startswith('Operation'):
        operation = x.split('=')[1].strip().split(' ')
        monkey['adding'] = operation[1] == '+'
        monkey['mult_self'] = operation[2] == 'old'
        monkey['op_amt'] = int(operation[2]) if not monkey['mult_self'] else -1
    elif x.startswith('Test'):
        monkey['test'] = int(x.split('by')[1].strip())
    elif 'true' in x:
        monkey['true_monkey'] = int(x.split('monkey')[1].strip())
    elif 'false' in x:
        monkey['false_monkey'] = int(x.split('monkey')[1].strip())

if monkey:
    monkeys.append(monkey)

common = 1
for monkey in monkeys:
    common *= monkey['test']

for _ in range(0, ROUNDS):
    for monkey in monkeys:
        for item in monkey['items']:
            if monkey['adding']:
                item += monkey['op_amt']
            elif monkey['mult_self']:
                item *= item
            else:
                item *= monkey['op_amt']
            
            # item //= 3
            if item % monkey['test'] == 0:
                monkeys[monkey['true_monkey']]['items'].append(item % common)
            else:
                monkeys[monkey['false_monkey']]['items'].append(item % common)
            
            monkey['total_inspections'] += 1

        monkey['items'] = []

insp = [m['total_inspections'] for m in monkeys]
insp.sort()
insp.reverse()
top_monkeys = insp[:2]

biz = 1
for t in top_monkeys:
    biz *= t

print(f'\n\nmonkey business: ', biz)
