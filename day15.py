#!/usr/bin/env python3

with open("data_day15test.txt") as data_file:
    data = [x.strip() for x in data_file]

CHECK_Y = 2000000

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
    
print(f'done {readings}')


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

cave = [['.'] * (max_x - min_x + 1) for x in range(min_y, max_y + 1)]

for sensor, beacon in readings:
    print(f'\nsensor is {sensor}')
    print(f'beacon is {beacon}')
    cave[sensor[1]-min_y][sensor[0]-min_x] = 'S'
    cave[beacon[1]-min_y][beacon[0]-min_x] = 'B'

def print_cave():
    for c in cave:
        for s in c:
            print(s, end='')
        
        print('')

print_cave()
