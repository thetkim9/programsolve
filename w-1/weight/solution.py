def solution(weight):
    #1
    weight.sort()
    #2
    nums = [weight[0]]
    for i in range(len(weight)-1):
        nums.append(nums[i]+weight[i+1])
    #3
    for i in range(len(nums)-1):
        v = nums[i] + 1
        if weight[i+1]>v:
            return v
    return nums[len(weight)-1]+1
