from math import lcm
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_length = set()
        for n in nums:
            nums_length.add(len(str(n)))
        max_len = lcm(*nums_length)
        nums.sort(key=lambda x: int(
            str(x)*(max_len // len(str(x)))), reverse=True)
        while 1 < len(nums) and nums[0] == 0:
            nums.pop(0)

        return "".join(map(str, nums))


print(Solution().largestNumber([0, 0, 0, 0])
      )
