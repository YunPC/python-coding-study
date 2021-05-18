# 문제풀이

뭐라뭐라 써있지만 결국 0,1,2 요소만 갖는 리스트를 내장함수 없이 In-Place 방식으로 오름차순 정렬을 하면된다
당연히 뭐 다양한 정렬알고리즘으로 할 수도 있지만 요소가 세가지 밖에 없으니까 적당히 조건문을 통해 구현도 가능할 듯 하다. 나는 한 번은 왼쪽에서 한번은 오른쪽에서 순회를 한해서 왼쪽에서 순회할 때 2가 있으면 끝으로 오른쪽으로 순회할 때 0이 있으면 시작으로 보냈다.

```python
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
```

이것 외에도 0과 1과 2의 갯수를 세서 배열을 전부 다시할당하는 방법들도 있다.
