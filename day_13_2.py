with open('input.txt', 'r') as file:
    text = file.read().strip().replace('\n\n', '\n')
    text += '\n[[2]]'
    text += '\n[[6]]'
    content = [eval(line) for line in text.split('\n')]

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

# le bubble sort because python got
# rid of cmp for sorting lists

for i in range(len(content)):
    for j in range(i + 1, len(content)):
        if cmp(content[i], content[j]) == 1:
            content[i], content[j] = content[j], content[i]

result = 1

for i, v in enumerate(content):
    if v == [[2]] or v == [[6]]:
        result *= i + 1

print(result)
