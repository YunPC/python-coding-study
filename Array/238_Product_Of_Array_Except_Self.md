# 풀이

## solution1

```python
def solution1(nums):

    zero_ind = -1

    for ind, num in enumerate(nums):
        if num == 0 and zero_ind == -1:
            zero_ind = ind
        elif num == 0 and zero_ind != -1:
            return [0 for _ in range(len(nums))]


    mul = 1
    # There is no zero
    if zero_ind == -1:
        
        for num in nums:
            mul *= num

        return [mul//num for num in nums]

    # There is one zero
    for num in nums:
        mul = mul * num if num != 0 else mul

    return [mul if num == 0 else 0 for num in nums]
```

0의 개수에 따라 동작을 달리한다.
1. 배열 내에 0이 두개라면 모든 요소가 0일 수 밖에 없으므로 0이 든 배열을 반환한다.

2. 0이 하나도 존재하지 않는다면 모든 요소의 곱을 구한 뒤, 한 요소씩 나누어서 값을 구한다.

3. 0이 하나 존재한다면 0을 제외한 모든 인덱스는 결과값이 0이어야 한다. 0이 든 인덱스에는 0을 제외한 요소의 곱을 담는다.

## solution2

```python
def solution2(nums):
    out = []
    p = 1
    
    #left multiply
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    
    p = 1

    for i in range(len(nums) -1, -1, -1):
        out[i] = out[i]*p
        p = p * nums[i]
    return out
```
왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈한다.