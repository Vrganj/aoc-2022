with open('input.txt', 'r') as file:
    content = file.readlines()

def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27
    return 0

result = 0

for rucksack in content:
    half = len(rucksack) // 2
    left, right = rucksack[:half], rucksack[half:]

    for element in set(left).intersection(set(right)):
        result += priority(element)

print(result)
