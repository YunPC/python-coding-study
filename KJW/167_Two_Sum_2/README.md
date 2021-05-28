# 문제 풀이

비내림차순 배열과 목표값을 받아 배열중 목표값이 되는 요소의 인덱스 두개를 1부터 카운팅해서 배열로 반환한다.

투포인터를 사용해서 그냥 풀었다

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
                continue
            if numbers[left] + numbers[right] > target:
                right -= 1
                continue
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
        return False
```