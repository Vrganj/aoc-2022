from math import prod

with open('input.txt', 'r') as file:
    content = file.read().strip().split('\n\n')

monkeys = list()

def parse_operation(operation):
    op, arg = operation.split(' ')

    if arg == 'old':
        if op == '+':
            return lambda n: n + n
        elif op == '*':
            return lambda n: n * n
    else:
        arg = int(arg)

        if op == '+':
            return lambda n: n + arg
        elif op == '*':
            return lambda n: n * arg
    

for part in content:
    monkey = dict()

    lines = part.splitlines()

    monkey['items'] = list(map(int, lines[1].strip().removeprefix('Starting items: ').split(', ')))
    monkey['operation'] = parse_operation(lines[2].strip().removeprefix('Operation: new = old '))
    monkey['divisible'] = int(lines[3].strip().removeprefix('Test: divisible by '))
    monkey['true'] = int(lines[4].strip().removeprefix('If true: throw to monkey '))
    monkey['false'] = int(lines[5].strip().removeprefix('If false: throw to monkey '))
    monkey['inspections'] = 0

    monkeys.append(monkey)

for round in range(20):
    for monkey in monkeys:
        monkey['inspections'] += len(monkey['items'])

        while len(monkey['items']):
            item = monkey['items'].pop(0)

            item = monkey['operation'](item) // 3
        
            if item % monkey['divisible'] == 0:
                monkeys[monkey['true']]['items'].append(item)
            else:
                monkeys[monkey['false']]['items'].append(item)

print(prod(sorted([m['inspections'] for m in monkeys], reverse=True)[:2]))
