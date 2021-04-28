def solution1(nums):

    zero_ind = -1

    for ind, num in enumerate(nums):
        if num == 0 and zero_ind == -1:
            zero_ind = ind
        elif num == 0 and zero_ind != -1:
            return [0 for _ in range(len(nums))]


    mul = 1
    # There is no zero
    if zero_ind == -1:
        
        for num in nums:
            mul *= num

        return [mul//num for num in nums]

    # There is one zero
    for num in nums:
        mul = mul * num if num != 0 else mul

    return [mul if num == 0 else 0 for num in nums]


def solution2(nums):
    out = []
    p = 1
    
    #left multiply
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    
    p = 1

    for i in range(len(nums) -1, -1, -1):
        out[i] = out[i]*p
        p = p * nums[i]
    return out
    
    