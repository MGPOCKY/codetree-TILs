dx = [1, 0]
dy = [0, 1]

N = int(input())
board = []
for i in range(N):
    lst = list(map(int, input().split()))
    board.append(lst)
maxVals = [[float('-inf') for _ in range(N)] for _ in range(N)]
maxVals[0][0] = board[0][0]

for y in range(N):
    for x in range(N):
        for i in range(2):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx and tx < N and 0 <= ty and ty < N:
                if tx > 0:
                    maxVals[ty][tx] = max(maxVals[ty][tx], maxVals[ty][tx - 1] + board[ty][tx])
                if ty > 0:
                    maxVals[ty][tx] = max(maxVals[ty][tx], maxVals[ty - 1][tx] + board[ty][tx])

print(maxVals[N-1][N-1])