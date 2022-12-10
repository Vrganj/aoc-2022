with open('input.txt', 'r') as file:
    content = file.readlines()

n = len(content)
m = len(content[0].strip())

def invisible(r, c):
    height = content[r][c]

    top = any(content[i][c] >= height for i in range(0, r))
    bottom = any(content[i][c] >= height for i in range(n - 1, r, -1))
    left = any(content[r][i] >= height for i in range(0, c))
    right = any(content[r][i] >= height for i in range(m - 1, c, -1))

    return top and bottom and left and right
    
result = 0

for r in range(n):
    for c in range(m):
        result += not invisible(r, c)

print(result)
