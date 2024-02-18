n, s = list(map(int, input().split()))
lst = list(map(int, input().split()))
idx = 0
result = float('inf')

global dp
dp = [0 for _ in range(n)]
dp[0] = lst[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + lst[i]

def getSubSum(a, b):
    if a > 0:
        return dp[b] - dp[a - 1]
    else:
        return dp[b]

for start in range(n):
    while True:
        if idx >= n:
            break
        subSum = getSubSum(start, idx)
        if subSum >= s:
            result = min(result, idx - start + 1)
            break
        else:
            idx = idx + 1

print(result if result != float('inf') else -1)