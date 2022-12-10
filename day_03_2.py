with open('input.txt', 'r') as file:
    content = file.readlines()

def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27
    return 0

result = 0
it = iter(content)

for a, b, c in zip(it, it, it):
    common = set(a).intersection(set(b), set(c)) - {'\n'}
    result += priority(common.pop())

print(result)
