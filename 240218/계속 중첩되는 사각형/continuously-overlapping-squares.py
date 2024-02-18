n = int(input())

# 0 => Empty & 1 => Red & 2 => Blue

board = [[0 for _ in range(201)] for _ in range(201)]
for i in range(n):
    x1, y1, x2, y2 = list(map(lambda val: val + 100, list(map(int, input().split()))))
    color = 1 if i % 2 == 0 else 2
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = color

result = 0
for y in range(201):
    for x in range(201):
        if board[y][x] == 2:
            result = result + 1

print(result)