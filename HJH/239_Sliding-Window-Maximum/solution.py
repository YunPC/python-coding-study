from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        start = 0
        
        while start + k <= len(nums):
            
            res.append(max(nums[start:start+k]))
            start += 1
        
        return res