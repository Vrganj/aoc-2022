with open('input.txt', 'r') as file:
    content = file.read().strip()

for i in range(14, len(content)):
    if len(set(content[i-14:i])) == 14:
        print(i)
        break
