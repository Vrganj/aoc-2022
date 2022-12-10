with open('input.txt', 'r') as file:
    content = file.readlines()

def parse(r):
    l, r = map(int, r.split('-'))
    return (l, r)

def overlaps(a, b):
    return (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1]) or (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1])

result = 0

for line in content:
    l, r = map(parse, line.split(','))

    if overlaps(l, r):
        result += 1

print(result)
