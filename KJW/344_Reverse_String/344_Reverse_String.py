
# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s) -> None:
        i = 0
        j = len(s)-1
        while i < j:  # 끝점과 시작점이 교차되기 전까지 반복
            s[i], s[j] = s[j], s[i]  # 시작점과 끝점의 문자를 교체
            i += 1  # 포인터를 중앙으로 한 칸씩 이동
            j -= 1


strings = ["h", "e", "l", "l", "o"]
Solution().reverseString(strings)
print(strings)  # ["o","l","l","e","h"]

strings = ["H", "a", "n", "n", "a", "h"]
Solution().reverseString(strings)
print(strings)  # ["h","a","n","n","a","H"]
