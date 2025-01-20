nums = [1, 2, 3, 4, 5]
target = 9
def twosum(nums, target):
    out = []
    for i in range(len(nums)):
        for j in range(i):
            if(nums[i] + nums[j] == target):
                out.append(j)
                out.append(i)
                return out

twosum(nums, target)