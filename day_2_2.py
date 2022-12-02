with open('input.txt', 'r') as file:
    content = file.readlines()

score = 0

worth = {
    'A': 1,
    'B': 2,
    'C': 3,
}

opposite = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

for line in content:
    a, b = line.strip().split()

    if b == 'X':
        b = opposite[opposite[a]]
    elif b == 'Y':
        b = a
        score += 3
    elif b == 'Z':
        b = opposite[a]
        score += 6

    score += worth[b]

print(score)