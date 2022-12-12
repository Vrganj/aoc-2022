from collections import deque

with open('input.txt', 'r') as file:
    content = file.readlines()

for i, line in enumerate(content):
    if 'S' in line:
        start = (i, line.find('S'))
        content[i] = content[i].replace('S', 'a')
    
    if 'E' in line:
        end = (i, line.find('E'))
        content[i] = content[i].replace('E', 'z')

rows = len(content)
cols = len(content[0])

cache = [[-1]*cols for _ in range(rows)]
queue = deque([start])
cache[start[0]][start[1]] = 0

mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]

while len(queue):
    current = queue.popleft()

    for (dx, dy) in zip(mx, my):
        next = (current[0] + dx, current[1] + dy)

        if 0 <= next[0] < rows and 0 <= next[1] < cols:
            if cache[next[0]][next[1]] != -1:
                continue

            if (ord(content[next[0]][next[1]]) > ord(content[current[0]][current[1]]) + 1):
                continue

            cache[next[0]][next[1]] = cache[current[0]][current[1]] + 1
                
            queue.append(next)

print(cache[end[0]][end[1]])
