# naive
def threeSum(nums):
    answer = set()
    nums.sort()

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s > 0:
                right -= 1
            elif s < 0:
                left += 1
            else:
                answer.add(tuple([nums[i], nums[left], nums[right]]))
                left += 1
                right -= 1

    answer = [list(x) for x in answer]

    return answer


# progressive
def threeSum2(nums):
    answer = set()
    nums.sort()

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s > 0:
                right -= 1
            elif s < 0:
                left += 1
            else:
                answer.add(tuple([nums[i], nums[left], nums[right]]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return answer


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum2([-1, 0, 1, 2, -1, -4]))
