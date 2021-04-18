class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):

            # len(s) right 를 가는 이유 -> right - 1 로 비교를 하기 때문에
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1

            # print(left, right, left + 1, right - 1, s[left + 1 : right - 1])

            return s[left + 1: right]

        # 예외 처리
        if len(s) < 2 or s == s[::-1]:
            return s

        result = s[0]

        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result
