with open('input.txt', 'r') as file:
    content = file.readlines()

result = 0

x = 1
cycle = 0

for line in content:
    split = line.split()

    if split[0] == 'addx':
        amount = int(split[1])

        cycle += 1

        if (cycle - 20) % 40 == 0:
            result += cycle * x
        
        cycle += 1

        if (cycle - 20) % 40 == 0:
            result += cycle * x
        
        x += amount
    elif split[0] == 'noop':
        cycle += 1

print(result)
