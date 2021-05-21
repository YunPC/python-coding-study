from collections import deque
from random import randrange
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        j = len(nums)-1
        for _ in range(len(nums)):
            if nums[i] == 2:
                nums.append(nums.pop(i))
                continue
            i += 1
        for _ in range(len(nums)):
            if nums[j] == 0:
                nums.insert(0, nums.pop(j))
                continue
            j -= 1
