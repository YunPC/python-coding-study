# 17. Letter Combinations of a Phone Number

## 풀이

- 대놓고 완전 탐색 하라는 문제다. 문자는 3개 밖에 없고 숫자도 길어야 4개까지 밖에 안 온다. 전부 탐색해도 3의 4승인 81회 밖에 안 돌기 때문에 어떻게 최적화를 해야 할 것인가가 아닌 **어떻게 탐색 할 것인가** 에 대해서 생각해야 하는 문제로 확인했다.

- dfs 를 통해 백트래킹을 구현하면 가능하다. 백트래킹은 주로 재귀를 이용하는것이 편하기 때문에 재귀로 구현하려고 노력했다.

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 하나의 번호에 해당되는 문자가 여러개 있는 경우는 대부분 해시테이블을 써주는 것이 좋다. 가장 간단하면서도 문제를 푸는 사람의 해시 이해도를 평가하는데 자주 나오는 풀이법이다.
        word = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        answer = []

        # 그놈의 예외처리
        if digits == "":
            return []

        # 조합 생각하면 된다. 여기서는 굳이 따로 check 배열을 이용해서 돌아왔던 부분을 체크할 필요가 없다.
        def dfs(idx, output):
            if idx >= len(digits):
                answer.append(output)
                return

            for str in word[digits[idx]]:
                dfs(idx+1, output + str)

        dfs(0, "")

        return answer
```

# 46. Permutations

## 풀이

- 말 그대로 순열을 뽑아 내는 문제이다. 위 문제에서는 check 배열이 필요 없었지만 순열 문제에서는 check 배열이 필요하다. 만약 숫자를 한 번이라도 썻으면 다시 못 쓰기 때문이다.

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        # List Comprehension 을 통한 리스트 초기화 (False)
        check = [False for _ in range(len(nums))]

        def permu(output):
            # 탈출 조건으로, 만약 output 의 길이가 같아지면 append
            if len(output) == len(nums):
                answer.append(output)
                return

            for i in range(len(nums)):
                if check[i] is False:
                    # 먼저 True 로 설정해줘야 아래의 재귀 호출에서 True 인 상태로 진행된다.
                    check[i] = True
                    permu(output + [nums[i]])
                    # 백트래킹 기법이라고 하는데, 한 번 왔던 숫자를 다시 False 처리 해줘야만 1-2-3 에서 끝나지 않고 1-3-2 진행이 가능해진다.
                    check[i] = False

        permu([])

        return answer

```
