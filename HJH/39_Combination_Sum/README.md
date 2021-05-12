## 풀이

### 39_Combination_Sum - 허재혁

> [https://leetcode.com/problems/combination-sum](https://leetcode.com/problems/combination-sum)

> 숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다.

**나의 풀이**
```python
class Solution:

    # Runtime 84 ms / Memory 14.4 MB
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(s, idx, combi):
            if s > target:
                return
            elif s == target:
                answer.append(combi)
                return

            for i in range(idx, len(candidates)):
                dfs(s + candidates[i], i, combi + [candidates[i]])

        dfs(0, 0, [])

        return answer
```

문제풀이전략
- dfs 문제다.
- candidates 내의 요소는 중복이 가능하므로 dfs의 탈출 조건을 합이 target보다 크거나 같을 경우로 설정해주어야 한다. 그것이 문제의 조건이기도 하다.
- 합(s)이 target보다 클 경우 더 이상 확인할 사항이 없기 때문에 재귀 호출을 중단한다. 조합의 합이 target과 같은 경우 해당 조합을 answer에 추가한다.
- 조합 문제이므로 dfs 재귀 for 문의 범위의 시작을 idx로 한다. 0으로 시작하면 순열에 해당한다.
- dfs함수의 인수로 초기 합(0), 최초 인덱스(0), 빈 조함([])을 넘겨준다.
*Runtime 84 ms / Memory 14.4 MB*
  
책의 풀이도 이와 유사하다.