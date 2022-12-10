with open('input.txt', 'r') as file:
    content = file.read().strip()

for i in range(4, len(content)):
    if len(set(content[i-4:i])) == 4:
        print(i)
        break
