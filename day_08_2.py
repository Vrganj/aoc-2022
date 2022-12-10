with open('input.txt', 'r') as file:
    content = file.readlines()

n = len(content)
m = len(content[0].strip())

def score(r, c):
    height = content[r][c]

    top = 0
    bottom = 0
    left = 0
    right = 0

    for i in range(r - 1, -1, -1):
        top += 1
        if content[i][c] >= height:
            break

    for i in range(r + 1, n):
        bottom += 1
        if content[i][c] >= height:
            break
    
    for i in range(c - 1, -1, -1):
        left += 1
        if content[r][i] >= height:
            break
    
    for i in range(c + 1, m - 1):
        right += 1
        if content[r][i] >= height:
            break
    
    return top * bottom * left * right
    
result = 0

for r in range(n):
    for c in range(m):
        result = max(result, score(r, c))

print(result)
