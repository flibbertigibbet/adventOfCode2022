#!/usr/bin/env python3

with open("data_day15.txt") as data_file:
    data = [x.strip() for x in data_file]

CHECK_ROW = 2000000

readings = []
for x in data:
    sensor, beacon = x.split(':')
    sensor_x, sensor_y = sensor.strip('Sensor at ').split(',')
    beacon_x, beacon_y = beacon.strip(' closest beacon is at').split(',')
    sensor_x = int(sensor_x.strip().strip('x='))
    sensor_y = int(sensor_y.strip().strip('y='))
    beacon_x = int(beacon_x.strip().strip('x='))
    beacon_y = int(beacon_y.strip().strip('y='))
    readings.append(((sensor_x, sensor_y), (beacon_x, beacon_y)))
    
print(f'read {readings}')


min_x = 0
min_y = 0
max_x = 0
max_y = 0

for p in readings:
    for x, y in p:
        if x < min_x:
            min_x = x
        
        if x > max_x:
            max_x = x
        
        if y < min_y:
            min_y = y
        
        if y > max_y:
            max_y = y

print(f"min x {min_x} max x {max_x} min y {min_y} max y {max_y}")

max_dist = 0
sensors = []
filled = {}
for sensor, beacon in readings:
    sensors.append(sensor)
    filled[f'{sensor[1]-min_y}:{sensor[0]-min_x}'] = 'S'
    filled[f'{beacon[1]-min_y}:{beacon[0]-min_x}'] = 'B'
    max_range = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1]) + 1
    if max_range > max_dist:
        max_dist = max_range

print(f'Max distance is {max_dist}')

def sensor_range(sensor, beacon):
    max_range = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1]) + 1
    print(f'Max range of sensor {sensor} is {max_range}')
    box_x_min = sensor[0] - max_range
    box_x_max = sensor[0] + max_range
    for x in range(box_x_min, box_x_max + 1):
        cy = CHECK_ROW - min_y
        cx = x - min_x
        dist = abs(x - sensor[0]) + abs(CHECK_ROW - sensor[1])
        if f'{cy}:{cx}' not in filled and dist < max_range:
            filled[f'{cy}:{cx}'] = '#'

min_row = CHECK_ROW - max_dist
max_row = CHECK_ROW + max_dist
for sensor, beacon in readings:
    if sensor[1] >= min_row and sensor[1] <= max_row:
        print(f'sensor {sensor} is in range {min_row}-{max_row}')
        sensor_range(sensor, beacon)
    else:
        print(f'skipping out-of-range sensor {sensor}')

no_beacon = 0
for i in range(min_x, max_x+1):
    if f'{CHECK_ROW-min_y}:{i}' in filled:
        no_beacon += 1

def print_filled():
    for i, x in enumerate(range(min_x, max_x-min_x+1)):
        print(f'\n{i+min_x}'.ljust(4, ' '), end='')
        for y in range(min_y, max_y-min_y+1):
            if f'{x}:{y}' in filled:
                print(filled[f'{x}:{y}'], end='')
            else:
                print('.', end='')

#print_filled()
print(f'\n\n{no_beacon} spots on row {CHECK_ROW} with no beacon\n')

