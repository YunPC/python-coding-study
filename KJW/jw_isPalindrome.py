# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_2 = ""
        for a in s:  # 입력받은 문자열을 하나씩 확인
            if a.isalnum():  # 문자열이 알파벳이나 숫자라면
                if a.isupper():  # 대문자라면
                    s_2 += a.lower()  # 소문자로 바꿔서 추가
                else:  # 대문자가 아니라면
                    s_2 += a  # 그냥 추가
        i = 0
        j = len(s_2)-1
        while i < j:  # 끝점과 시작점이 교차되기 전까지 반복
            if s_2[i] != s_2[j]:  # 양 끝단의 문자가 다르다면
                return False  # 거짓
            i += 1  # 포인터를 중앙으로 한칸씩 이동
            j -= 1
        return True  # 모든 검사가 끝나면 참


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))  # True
print(Solution().isPalindrome('race a car'))  # False
