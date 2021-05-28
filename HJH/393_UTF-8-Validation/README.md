# 풀이

## ![https://leetcode.com/problems/utf-8-validation/](https://leetcode.com/problems/utf-8-validation/) - 허재혁

### 나의 풀이

```python
import re

class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        data = list(map(lambda x: bin(x)[2:], data))
        data = list(map(lambda x: '0'*(8 - len(x)) + x, data))

        one_bit_reg = ["^0"]
        two_bit_reg = ["^110", "^10"]
        three_bit_reg = ["^1110", "^10", "^10"]
        four_bit_reg = ["^11110", "^10", "^10", "^10"]

        curr = 0
        while curr < len(data):
            if re.search("^11110", data[curr]):
                for i in range(4):
                    if curr + i >= len(data) or re.search(four_bit_reg[i], data[curr + i]) is None:
                        return False
                curr += 4
            elif re.search("^1110", data[curr]):
                for i in range(3):
                    if curr + i >= len(data) or re.search(three_bit_reg[i], data[curr + i]) is None:
                        return False
                curr += 3
            elif re.search("^110", data[curr]):
                for i in range(2):
                    if curr + i >= len(data) or re.search(two_bit_reg[i], data[curr + i]) is None:
                        return False
                curr += 2
            elif re.search("^0", data[curr]):
                for i in range(1):
                    if curr + i >= len(data) or re.search(one_bit_reg[i], data[curr + i]) is None:
                        return False
                curr += 1
            else:
                return False


        return True
```

- 첫 번째 숫자의 bin()값을 정규표현식(re 모듈)을 이용하여 필터링하여 byte를 선택한다.
- 해당 byte의 규칙을 적용해보면서 유효성을 검사한다.
- Runtime 216 ms / Memory 15.6 MB

### solution

```python
        start = 0

        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True
```

- 비트마스크를 이용한 풀이다.
- Runtime 112 ms / Memory 14.5 MB
