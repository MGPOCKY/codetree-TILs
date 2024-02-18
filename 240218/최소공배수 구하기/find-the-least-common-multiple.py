n, m = list(map(int, input().split()))

mul = 1
while True:
    val = n * mul
    if val % m == 0:
        break
    else:
        mul = mul + 1

print(n * mul)