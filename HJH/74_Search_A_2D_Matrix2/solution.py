from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False

        top = 0
        bottom = len(matrix) - 1
        
        while top < bottom:
            mid = (top + bottom) // 2
            
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid + 1][0]:
                bottom = mid

        left = 0
        right = len(matrix[top]) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if target > matrix[top][mid]:
                left = mid + 1
            elif target < matrix[top][mid]:
                right = mid
            else:
                return True
        
        if matrix[top][left] == target:
            return True

        return False

if __name__ == '__main__':
    print(Solution().searchMatrix([[1], [3], [5]], 3))
    print(Solution().searchMatrix([[1]], 1))
