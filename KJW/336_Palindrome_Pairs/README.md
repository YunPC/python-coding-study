# 문제풀이

> 배열로 받은 문자열들의 조합중 펠린드롬이 되는 조합의 인덱스를 쌍으로 반환하라

일단 브루트포스

```python
class Solution:
    def isPalindrome(self, word1, word2):
        fullword = word1+word2
        i = 0
        j = len(fullword)-1
        while i < j:
            if fullword[i] != fullword[j]:
                return False
            i += 1
            j -= 1
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        for idx in range(len(words)):
            for idx2 in range(len(words)):
                if idx == idx2:
                    continue
                if self.isPalindrome(words[idx], words[idx2]):
                    res.append([idx, idx2])
        return res
```

당연히 실패했다 ㅋ

그래서 문자열의 가장 뒷 문자로 딕셔너리를 만들어서 비교하는 경우의 수를 줄였다. 중간에 빈 문자열에 대한 예외처리도 추가했다

```python
class Solution:
    def isPalindrome(self, word):
        return word == word[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        blank_idx = False
        lastword = defaultdict(list)
        for idx, word in enumerate(words):
            if word == "":
                blank_idx = idx
                continue
            lastword[word[-1]].append([idx, word])

        for idx, word in enumerate(words):
            if word == "":
                continue
            for word2 in lastword[word[0]]:
                if idx == word2[0]:
                    continue
                if self.isPalindrome(word+word2[1]):
                    res.append([idx, word2[0]])
            if blank_idx is not False and self.isPalindrome(word):
                res.append([idx, blank_idx])
                res.append([blank_idx, idx])
        return res
```

이렇게 하면 8% 정도로 통과가 되긴 한다... 그런데 매우 찜찜 총 2264ms가 걸린다... 속도를 어떻게 단축할 수 있을까?

어 근데 생각해 보니 이건 트라이 문제였다.. Trie를 사용하는 방법을 생각 해 보자.

그런데 생각이 안나기 때문에 교재를 참고했다.

그런데 교재를 봐도 뭔소린지를 모르겠다...

일단 풀었으니 이건 같이 이야기 해보는 건 어떨까? ㅎㅎ...
