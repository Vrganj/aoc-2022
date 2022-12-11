from math import prod
from collections import deque

with open('input.txt', 'r') as file:
    content = file.read().strip().split('\n\n')

monkeys = list()

def parse_operation(operation):
    op, arg = operation.split(' ')

    if arg == 'old':
        arg = '0'

    if op == '+':
        return -int(arg)
    elif op == '*':
        return int(arg)

for part in content:
    monkey = dict()

    lines = part.splitlines()

    monkey['items'] = deque([-int(i)] for i in lines[1].strip().removeprefix('Starting items: ').split(', '))
    monkey['operation'] = parse_operation(lines[2].strip().removeprefix('Operation: new = old '))
    monkey['divisible'] = int(lines[3].strip().removeprefix('Test: divisible by '))
    monkey['true'] = int(lines[4].strip().removeprefix('If true: throw to monkey '))
    monkey['false'] = int(lines[5].strip().removeprefix('If false: throw to monkey '))
    monkey['inspections'] = 0

    monkeys.append(monkey)

for round in range(10000):
    print(round)
    for monkey in monkeys:
        monkey['inspections'] += len(monkey['items'])

        while len(monkey['items']):
            item = monkey['items'].popleft()
            item.append(monkey['operation'])
            
            div = monkey['divisible']
            start = 0

            for part in item:
                if part < 0:
                    start = (start + ((-part) % div)) % div
                elif part > 0:
                    start = (start * (part % div)) % div
                else:
                    start = (start * (start % div)) % div
                
            if start == 0:
                monkeys[monkey['true']]['items'].append(item)
            else:
                monkeys[monkey['false']]['items'].append(item)


print(prod(sorted([m['inspections'] for m in monkeys], reverse=True)[:2]))
