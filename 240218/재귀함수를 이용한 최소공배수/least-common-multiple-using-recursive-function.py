def recursion(nums, val):
    isAllSatisfy = True
    for num in nums:
        if val % num != 0:
            isAllSatisfy = False
    if isAllSatisfy:
        return val
    else:
        return recursion(nums, val + nums[0])

n = int(input())
nums = list(map(int, input().split()))
print(recursion(nums, nums[0]))