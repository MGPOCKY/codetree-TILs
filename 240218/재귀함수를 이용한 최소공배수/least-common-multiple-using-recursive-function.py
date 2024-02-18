import sys
sys.setrecursionlimit(100000)

def recursion(nums, val):
    isAllSatisfy = True
    for num in nums:
        if val % num != 0:
            isAllSatisfy = False
    if isAllSatisfy == True:
        return val
    else:
        return recursion(nums, val + 1)

n = int(input())
nums = list(map(int, input().split()))
print(recursion(nums, 1))