#!/usr/bin/env python3

with open("data_day16test.txt") as data_file:
    data = [x.strip() for x in data_file]
    
print(f'loaded {data}')

valves = {}
for x in data:
    valve, tunnels = x.split(';')
    valve_parts = valve.split(' ')
    print(tunnels)
    valves[valve_parts[1]] = {
        'rate': int(valve_parts[4].strip('rate=')),
        'tunnels': tunnels.split('valve')[1].strip('s').strip().split(', '),
        'open': False
    }

print(valves)

START_VALVE = 'AA'
TIME_LIMIT = 30

cur_valve = START_VALVE
remaining_time = TIME_LIMIT
released = 0

while remaining_time > 0:
    valve = valves[cur_valve]
    cur_rate = valve['rate']
    if cur_rate > 0 and not valve['open']:
        print(f'release valve {cur_valve} with rate {cur_rate}')
        valve['open'] = True
        released += cur_rate * remaining_time
        remaining_time -=1
    else:
        print(f'NOT releasing {valve}')
        valve['open'] = True # release zero-rate valves to mark visited
    
    next_valves = [valves[v]['rate'] for v in valve['tunnels'] if not valves[v]['open']]
    if len(next_valves) > 0:
        next_tunnel_max = max(next_valves)
    else:
        next_tunnel_max = # FIXME
    next_tunnel = None
    for t in valve['tunnels']:
        tunnel = valves[t]
        if tunnel['rate'] == next_tunnel_max:
            next_tunnel = t
            break
    
    if remaining_time > 0:
        print(f'moving to {next_tunnel}')
        cur_valve = next_tunnel
        remaining_time -=1

print(f'released {released} pressure before time reached {remaining_time}')
