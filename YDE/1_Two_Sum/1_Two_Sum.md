# 풀이

## 브루트 포스로 계산

```python
# 부르트 포스로 계산

def solution1(nums, target):
    answer = []
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                answer.append([i, j])

    return answer

print(solution1([2, 7, 11, 15], 9))
```

모든 경우의 수를 조합하여 문제를 계산한다. 이 경우 반복문을 2중으로 돌기 때문에 시간복잡도가 O(n^2)이다.

## in을 이용한 탐색

```python
# in을 이용한 탐색

def solution2(nums, target):
    answer = []
    length = len(nums)
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)

    return answer
```
i번째 수를 뺀 값이 리스트에 있는지 확인하는 코드이다. 시간복잡도는 똑같지만, 파이썬에서는 in이 더 빠르게 동작하기 때문에 실제 시간은 감소한다.

## 첫번째 수를 뺀 결과 키 조회

```python
def solution3(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]
```
숫자를 키로하고 인덱스를 값으로 하는 딕셔너리를 생성한다. 이후, 타겟 넘버를 제거한 값이 딕셔너리에 있는지 확인하면 O(n)으로 시간복잡도를 단축할 수 있다.

## 조회 결과 개선

```python
def solution4(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
```
위의 코드를 for문 하나로 담은 것이다. 실제 걸리는 시간엔 별 차이가 없다.

## 투 포인터 이용

```python
# 투 포인터 이용(정렬된 경우만 가능!)
    
def solution5(nums, target):
    left, right = 0, len(nums) -1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return left, right
```
양쪽의 합과 타겟넘버를 비교하면 작으면 왼쪽 인덱스를 증가하고 크면 오른쪽 인덱스를 감소시키는 코드이다. 이 경우 값이 오름차순이라고 보장되어있지 않기 때문에 사용할 수 없다.