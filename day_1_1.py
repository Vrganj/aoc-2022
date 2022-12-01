with open('input.txt', 'r') as file:
    content = file.read().strip()

result = 0

for section in content.split('\n\n'):
    result = max(result, sum(map(int, section.split())))

print(result)
