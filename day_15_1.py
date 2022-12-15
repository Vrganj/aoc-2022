from collections import namedtuple
import re

Point = namedtuple('Point', 'x y')

with open('input.txt', 'r') as file:
    content = file.readlines()

points = set()

for line in content:
    sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))

    points.add((Point(sx, sy), Point(bx, by)))

    distance = abs(sx - bx) + abs(sy - by)

y = 2000000

result = []

def validate(sequence):
    if sequence[1] < sequence[0]:
        return None
    return sequence

for sensor, beacon in points:
    distance = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
    offset = abs(sensor.y - y)

    length = distance - offset

    if length >= 0:
        if beacon.y == y:
            result.append(validate((sensor.x - length, beacon.x - 1)))
            result.append(validate((beacon.x + 1, sensor.x + length)))
        else:
            result.append((sensor.x - length, sensor.x + length))

def union(a, b):
    if a == None and b == None:
        return None
    elif a == None:
        return b
    elif b == None:
        return a
    elif a[0] <= b[0] <= a[1] <= b[1]:
        return (a[0], b[1])
    elif b[0] <= a[0] <= b[1] <= a[1]:
        return (b[0], a[1])
    elif a[0] <= b[0] <= b[1] <= a[1]:
        return a
    elif b[0] <= a[0] <= a[1] <= b[1]:
        return b
    else:
        return [a, b]

def includes(intervals, element):
    for interval in intervals:
        if interval == None: continue
        if interval[0] <= element <= interval[1]:
            return True
    return False

def length(interval):
    if interval == None:
        return 0

    return interval[1] - interval[0] + 1

for i in range(len(result)):
    for j in range(len(result)):
        u = union(result[i], result[j])

        if type(u) == tuple:
            result[j] = None
            result[i] = u

solution = sum(map(length, result))

print(solution)
