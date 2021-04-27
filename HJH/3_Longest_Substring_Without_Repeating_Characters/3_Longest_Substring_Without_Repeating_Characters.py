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

    def two_pointer_solution(self, s: str) -> int:
        max_length = start = 0
        used = {}
        for index, value in enumerate(s):
            if value in used and start <= used[value]:
                start = used[value] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[value] = index

        return max_length


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().two_pointer_solution("abcabcbb"))
print(Solution().two_pointer_solution("pwwkew"))
print(Solution().two_pointer_solution("dvdf"))
print(Solution().two_pointer_solution("bbbbb"))
