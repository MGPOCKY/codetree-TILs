n, m = list(map(int, input().split()))
lst = list(map(int, input().split()))
sumOfLst = 0
idx = 0
result = 0

for i in range(n):
    while True:
        if sumOfLst == m:
            result = result + 1
            break
        if sumOfLst < m:
            if idx >= i and idx < n:
                sumOfLst = sumOfLst + lst[idx]
            if idx >= n:
                break
            idx = idx + 1
        if sumOfLst > m:
            break
    
    sumOfLst = sumOfLst - lst[i]

print(result)