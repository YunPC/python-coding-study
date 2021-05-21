from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        
        curr = 0
        while True:
            if curr >= len(intervals) - 1:
                return intervals                
            if intervals[curr][1] >= intervals[curr + 1][0]:
                popped = intervals.pop(curr + 1)
                if intervals[curr][1] < popped[1]:
                    intervals[curr][1] = popped[1]
            else:
                curr += 1