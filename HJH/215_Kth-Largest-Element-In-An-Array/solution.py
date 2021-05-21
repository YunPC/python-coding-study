import heapq
from typing import List

class Solution:
    def naive(self, nums: List[int], k: int) -> int:
        heap = []
        
        while nums:
            num = nums.pop()
            heapq.heappush(heap, (-1 * num, num))
            
        cnt = 0
        while True:
            cnt += 1
            popped = heapq.heappop(heap)
            if cnt == k:
                return popped[1]


    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
    
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)