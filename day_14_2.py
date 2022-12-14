import time

with open('input.txt', 'r') as file:
    content = [line.split(' -> ') for line in file.readlines()]

space = set()

def inclusive(a, b):
    return range(min(a, b), max(a, b) + 1)

my = 0

for path in content:
    prev = None

    for x, y in [tuple(map(int, loc.split(','))) for loc in path]:
        space.add((x, y))

        if prev != None:
            for nx in inclusive(prev[0], x):
                for ny in inclusive(prev[1], y):
                    space.add((nx, ny))

        prev = (x, y)

        my = max(my, y)

for x in inclusive(0, 1000):
    space.add((x, my + 2))

result = 0

sand = (500, 0)

while True:
    if sand[1] >= 1000:
        print(result)
        break

    if (sand[0], sand[1] + 1) not in space:
        sand = (sand[0], sand[1] + 1)
    elif (sand[0] - 1, sand[1] + 1) not in space:
        sand = (sand[0] - 1, sand[1] + 1)
    elif (sand[0] + 1, sand[1] + 1) not in space:
        sand = (sand[0] + 1, sand[1] + 1)
    else:
        result += 1

        if sand == (500, 0):
            break

        space.add(sand)
        sand = (500, 0)

print(result)
