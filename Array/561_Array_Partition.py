# class Solution:
#     def arrayPairSum(self, nums) -> int:
#         nums.sort()
#         nums_partition = [[nums[i], nums[i+1]] for i in range(0, len(nums), 2)]
#         result = 0
#         for num_set in nums_partition:
#             result += num_set[0]
#         return result


class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))
