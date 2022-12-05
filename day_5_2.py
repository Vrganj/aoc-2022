with open('input.txt', 'r') as file:
    content = file.readlines()

values = [[] for _ in range(9)]

it = iter(content)

while True:
    line = next(it)[:-1]

    if not line:
        break
    
    for index, item in enumerate(line[1::4]):
        if not 'A' <= item <= 'Z':
            continue

        values[index].insert(0, item)

for line in it:
    split = line.strip().split()
    count, a, b = map(int, split[1::2])

    a, b = a - 1, b - 1

    intermediate = []

    for i in range(count):
        intermediate.append(values[a].pop())

    while len(intermediate):
        values[b].append(intermediate.pop())

print(''.join(stack[-1] for stack in values))