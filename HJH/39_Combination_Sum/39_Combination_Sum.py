from typing import List


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


print(Solution().combinationSum([2, 3, 6, 7], 7))
