dx = [1, 0]
dy = [0, 1]

n = int(input())
board = []
for _ in range(n):
    lst = list(map(int, input().split()))
    board.append(lst)
dp = [[[float('-inf'), float('inf'), float('inf')] for _ in range(n)] for _ in range(n)]
dp[0][0] = [board[0][0], board[0][0], 0]
for y in range(n):
    for x in range(n):
        for i in range(2):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx and tx < n and 0 <= ty and ty < n:
                if tx > 0:
                    pick = dp[ty][tx - 1]
                    newVal = [
                        max(pick[0], board[ty][tx]),
                        min(pick[1], board[ty][tx]),
                        abs(max(pick[0], board[ty][tx]) - min(pick[1], board[ty][tx]))]
                    if newVal[2] < dp[ty][tx][2]:
                        dp[ty][tx] = newVal
                if ty > 0:
                    pick = dp[ty - 1][tx]
                    newVal = [
                        max(pick[0], board[ty][tx]),
                        min(pick[1], board[ty][tx]),
                        abs(max(pick[0], board[ty][tx]) - min(pick[1], board[ty][tx]))]
                    if newVal[2] < dp[ty][tx][2]:
                        dp[ty][tx] = newVal

print(dp[n-1][n-1][2])