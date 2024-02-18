def recursion(val, decrease, maxV):
    for _ in range(val):
        print('*', end=' ')
    print()
    if val == 1 and decrease == True:
        recursion(val, False, maxV)
    elif decrease == False and maxV == val:
        return
    else:
        if decrease == True:
            recursion(val - 1, decrease, maxV)
        else:
            recursion(val + 1, decrease, maxV)

n = int(input())
recursion(n, True, n)