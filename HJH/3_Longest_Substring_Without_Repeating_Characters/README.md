## 풀이

### 30_Longest_Substring_without_repeating_characters(p. 303) - 허재혁

> [https://leetcode.com/problems/longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

> 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.

**나의 풀이**
```python
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        d1 = deque(s)
        d2 = deque()

        while d1:
            left_popped = d1.popleft()

            try:
                idx_found = d2.index(left_popped)
                for _ in range(idx_found + 1):
                    d2.popleft()
            except ValueError:
                pass

            d2.append(left_popped)
            answer = max(answer, len(d2))

        if d2:
            answer = max(answer, len(d2))

        return answer
```
문제 풀이 전략은 다음과 같다.
1. 두 개의 deque를 선언한다. 첫번째 deque(d1)에는 s의 문자들을 저장해놓고 다른 하나(d2)는 비워놓는다.
1. d1이 차있는 동안 while 문을 실행한다.
1. while 문의 로직은 다음과 같다.
    - left_popped에 d1의 앞쪽에서부터 하나씩 빼서 저장한다.
    - d2에서 left_popped의 인덱스를 찾는 index() 메소드를 실행한다.
    - index()는 찾으려는 값의 인덱스를 발견하지 못했을 때 즉시 ValueError를 발생시킨다. ValueError가 발생할 때, 즉 발견하지 못했을 때는 pass한다.
    - 발견했을 때 idx_found까지 popleft()한다.
    
1. d2에 left_popped를 추가한다.
1. answer는 현재 저장된 answer와 현재 d2에 저장된 요소의 개수 중 최대로 업데이트한다.
1. while문이 끝난 시점에 d2에 요소가 남아있을 수 있으므로, 위의 과정을 한번 더 진행한다.
- Runtime 76 ms / Memory 14.6 MB