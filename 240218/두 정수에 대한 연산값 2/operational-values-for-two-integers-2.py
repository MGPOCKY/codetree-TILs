def func(a, b):
    if a > b:
        return [a * 2, b + 10]
    else:
        return [a + 10, b * 2]

a, b = list(map(int, input().split()))
result = func(a, b)
print(result[0], result[1])