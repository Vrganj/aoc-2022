with open('input.txt', 'r') as file:
    content = file.readlines()

def parse(r):
    l, r = map(int, r.split('-'))
    return (l, r)

def includes(a, b):
    return a[0] <= b[0] and a[1] >= b[1]

result = 0

for line in content:
    l, r = map(parse, line.split(','))

    if includes(l, r) or includes(r, l):
        result += 1

print(result)
