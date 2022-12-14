with open('input.txt', 'r') as file:
    content = file.read().strip().split('\n\n')

def cmp(a, b):
    if type(a) == type(b) == int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    
    if type(a) == int and type(b) == list:
        return cmp([a], b)
    
    if type(a) == list and type(b) == int:
        return cmp(a, [b])

    index = 0

    while True:
        if index >= len(a) and index >= len(b):
            return 0

        if index >= len(a):
            return -1

        if index >= len(b):
            return 1
        
        result = cmp(a[index], b[index])

        if result != 0:
            return result

        index += 1

result = 0
    
for i, part in enumerate(content):
    left, right = map(eval, part.split('\n'))

    if cmp(left, right) == -1:
        result += i + 1

print(result)
