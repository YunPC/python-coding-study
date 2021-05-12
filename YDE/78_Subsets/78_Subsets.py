# Runtime: 32 ms
# Memory Usage: 14.5 MB
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        
        for i in range(1, len(nums)+1):
            
            for el in list(combinations(nums, i)):
                res.append(el)
                
        return res