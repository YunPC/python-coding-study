# 배열

LeetCode

1_Two_Sum

42_Trapping_Rain_Water

15_3Sum

561_Array_Partition

238_Product_of_Array_Except_Self

121_Best_Time_to_Buy_and_Sell_Stock

## 풀이

### 561_Array_Partition - 김정원

> 문제 : 짝수개의 숫자배열을 받은 뒤, 두개씩 짝을 지어 각 그룹에서 작은 값들을 모두 더했을 때 나올 수 있는 최대값을 구하기

**접근**
문제를 보고 먼저 떠올린 방법은 브루트 포스이지만, 분명히 최적의 방법이 있을 거라고 생각을 했다.
가장 기본적으로 모든 그룹에 _작은 값으로 들어갈 수 있는 가장 큰 값들_ 을 구해야 한다.
어떤 방법이 있을 수 있을까 생각했는데, 반 직관으로 배열을 오름차순으로 정렬했다, 배열이 오름차순으로 정렬하게 된다면 i와 i+1의 값은 배열 내에서 가장 인접하기 때문에 모든 그룹내에서 작은 값과 큰 값의 차이가 최소가 된다. 그렇다면 앞에서 말한 _작은 값으로 들어갈 수 있는 가장 큰 값_ 들을 찾을 수 있다, 그렇기 때문에 아래와 같이 풀이했다.

```python
class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        nums_partition = [[nums[i], nums[i+1]] for i in range(0, len(nums), 2)]
        result = 0
        for num_set in nums_partition:
            result += num_set[0]
        return result
```

1. 먼저 받은 배열을 오름차순으로 정렬한다
2. 그리고 해당 배열의 i와 i+1을 리스트로 묶어 새로운 리스트에 집어넣는다
3. 그리고 각 리스트의 0번 인덱스의 값을 합친 뒤 반환한다

**추가**
위의 방법으로 테스트를 통과할 수 있었지만, 생각 해 보면 어차피 오름차순으로 정렬되어 있기 때문에 홀수번째 값들을 더하기만 하면 된다. 그래서 아래의 코드만으로 끝낼 수 있다

```python
class Solution:
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
```
