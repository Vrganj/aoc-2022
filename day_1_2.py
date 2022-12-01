with open('input.txt', 'r') as file:
    content = file.read().strip()

elves = []

for section in content.split('\n\n'):
    elves.append(sum(map(int, section.split())))

elves.sort(reverse=True)

print(sum(elves[:3]))
