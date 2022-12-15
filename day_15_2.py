from collections import namedtuple
import re

Point = namedtuple('Point', 'x y')

with open('input.txt', 'r') as file:
    content = file.readlines()

pos_a = []
neg_a = []

points = set()

def get_a(line):
    return (line[1].y - line[0].y) // (line[1].x - line[0].x)

def get_b(line):
    return line[0].y - line[0].x * get_a(line)

def get_ab(line):
    return (get_a(line), get_b(line))

for line in content:
    sx, sy, bx, by = map(int, re.findall(r'(-?\d+)', line))

    distance = abs(sx - bx) + abs(sy - by)

    neg_a.append(get_b((Point(sx - distance, sy), Point(sx, sy - distance))))
    pos_a.append(get_b((Point(sx - distance, sy), Point(sx, sy + distance))))
    pos_a.append(get_b((Point(sx, sy - distance), Point(sx + distance, sy))))
    neg_a.append(get_b((Point(sx, sy + distance), Point(sx + distance, sy))))

    points.add((Point(sx, sy), Point(bx, by)))

for a in pos_a:
    for b in neg_a:
        x = (b - a) // 2
        y = x + a - 1

        if not ((0 <= x <= 4000000) and (0 <= y <= 4000000)):
            continue
        
        fail = False

        for sensor, beacon in points:
            d1 = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
            d2 = abs(sensor.x - x) + abs(sensor.y - y)

            if d2 <= d1:
                fail = True
                break
        
        if not fail:
            print(4000000 * x + y)
            exit(0)
