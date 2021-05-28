# 문제풀이

> 수로 된 리스트를 받아서 해당 수들의 조합중 가장 큰 값을 문자열로 반환하면 된다.
> 예 : [3,30,34,5,9] => "9534330"

결국 숫자들을 문자열로 합쳐서 반환하는 것이다. 연산은 하지 않고..
sort함수를 사용해 숫자를 문자열로 변경해서 정렬하고 어쩌구 저쩌구 하면 될 것 같은데 처음에는 접근이 어려웠다. 일단 문자열로 변경해서 내림차순 정렬을 하면

9 5 3 30 34 순으로 정렬이 된다. 그러나 당연히 이렇게하면 안된다.

비교를 할 때 34 3 30 순으로 되어야 하는데, 그렇게 할려면.. 어떻게 해야할까.
한가지 솔루션을 생각 한 것은 모든 값을 2자리로 치환하면 숫자값으로서 비교가 가능하다.

99 55 34 33 30 이런 식으로 한자리 수의 경우는 2자리로 강제로 변경해서 진행하면 된다.
값이 커져도 가능하다 예를들어

12 341 22 9 321 이렇게 리스트가 들어온다면 가장 큰 수는
"9 341 321 22 12" 이렇게 나올것이다. 그러나 이런 경우에는 값이 짤릴 수 있기 때문에 3자리로 맞출수가 없다. 그래서 모든 길이의 최소공배수를 구하여 그 값으로 나눈만큼 반복한다.. 위 리스트의 길이는 1, 2, 3이다 세 수의 최소공배수는 6이므로 모든 숫자를 6자리로 변경할 수 있다 그렇게되면
"999999 341341 321321 222222 121212" 이렇게 변경할 수 있고 이 숫자값의 대소관계를 비교해서 넘길 수 있다.

이런 로직을 통한 풀이는 아래와 같다

```python
from math import lcm
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_length = set()
        for n in nums:
            nums_length.add(len(str(n)))
        max_len = lcm(*nums_length)
        nums.sort(key=lambda x: int(
            str(x)*(max_len // len(str(x)))), reverse=True)
        while 1 < len(nums) and nums[0] == 0:
            nums.pop(0)

        return "".join(map(str, nums))
```

교재에서는 삽입정렬 알고리즘의 비교연산을 개조(?)해서 풀이했다. 만약 삽입정렬시 비교하는 대상과 앞뒤로 붙여보고 앞에 붙였을 때 값이 크다면, 앞으로 보내는 방식으로 진행했다. 엄밀히 말하면 이렇게가 맞지만 시간복잡도 상으로는 내 방법이 빨랐다 ㅋ

```python
class Solution:
    @staticmethod
    def to_swap(n1, n2):
        return str(n1)+str(n2) < str(n2)+str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        i=1

        while i < len(nums):
            j = i

            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))
```

내 풀이 : 28ms
교재 풀이 : 72ms
