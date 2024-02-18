from sys import stdin

n, m = list(map(int, stdin.readline().split()))
lst = list(map(int, stdin.readline().split()))
global dp
dp = [0 for _ in range(n)]
dp[0] = lst[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + lst[i]

def getSubSum(a, b):
    global dp
    if a > 0:
        return dp[b] - dp[a - 1]
    else:
        return dp[b]

for _ in range(m):
    a, b = list(map(lambda val: val - 1, list(map(int, stdin.readline().split()))))
    print(getSubSum(a, b))