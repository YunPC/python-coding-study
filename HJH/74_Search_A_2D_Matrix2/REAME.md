# 풀이

## ![https://leetcode.com/problems/search-a-2d-matrix/](https://leetcode.com/problems/search-a-2d-matrix/) - 허재혁

### 나의 풀이

```python
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
```

- 문제의 조건에 따라 이진 검색을 행에 대해, 열에 대해 두 번 반복하면 되는 문제이다.
- Runtime 48 ms / Memory 14.8 MB

### 답지의 풀이

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)
```

- 이진 검색 단원이나 답지는 이진검색으로 풀면 복잡하다고 한다. 음...(테스트 시 이런 것을 사전에 알고 풀 수 있을까?)
- any()를 사용하면 아주 간단하고 심플하게 풀 수 있긴 하다.
