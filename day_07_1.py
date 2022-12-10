import re

with open('input.txt', 'r') as file:
    content = re.findall(r'(\$[^$]+)', file.read().strip())

class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = dict()

root = File('/', 0, None)
current = root

for line in content[1:]:
    command, *output = line.strip().split('\n')
    command = command.split()[1:]

    if command[0] == 'cd':
        if command[1] == '..':
            current = current.parent
        else:
            current = current.children[command[1]]
    elif command[0] == 'ls':
        for row in output:
            a, b = row.split()
            size = 0 if a == 'dir' else int(a)
            current.children[b] = File(b, size, current)

result = 0

def dfs(file):
    global result
    
    size = 0

    for child in file.children.values():
        if child.size:
            size += child.size
        else:
            size += dfs(child)
    
    if size <= 100000:
        result += size

    return size

dfs(root)
print(result)
