K, N = list(map(int, input().split()))
it = [i + 1 for i in range(K)]

def backtrack(remain, it, lst):
    if remain == 0:
        for num in lst:
            print(num, end=" ")
        print()
    else:
        for num in it:
            newList = lst.copy()
            newList.append(num)
            backtrack(remain - 1, it, newList)

backtrack(N, it, [])