with open('input.txt', 'r') as file:
    content = file.readlines()

x = 1
cycle = 0

def draw():
    global x, cycle

    if (cycle % 40 - 1) <= x <= (cycle % 40 + 1):
        print('#', end='')
    else:
        print('.', end='')
    
    if (cycle + 1) % 40 == 0:
        print()
    
    cycle += 1


for line in content:
    split = line.split()

    if split[0] == 'addx':
        draw()
        draw()

        x += int(split[1])
    elif split[0] == 'noop':
        draw()
