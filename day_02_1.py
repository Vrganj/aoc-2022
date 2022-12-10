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

matching = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

for line in content:
    a, b = line.strip().split()

    score += worth[matching[b]]

    if a == matching[b]:
        score += 3
    elif matching[b] == opposite[a]:
        score += 6

print(score)