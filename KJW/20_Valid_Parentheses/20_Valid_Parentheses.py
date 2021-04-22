# 단순 IF문

class Solution:
    def isValid(self, s: str) -> bool:
        open_brakets = {"(", "{", "["}
        stack = []
        count = 0
        for b in s:  # 괄호를 순회하면서
            if b in open_brakets:  # 여는 괄호라면
                stack.append(b)
                count += 1
            else:  # 닫는 괄호이고
                if not stack:  # 스택이 비어있다면 False
                    return False
                # 닫을 수 있는 괄호라면 닫고 스택에서 제거
                if stack[-1] == "(" and b == ")":
                    stack.pop()
                    count -= 1
                elif stack[-1] == "{" and b == "}":
                    stack.pop()
                    count -= 1
                elif stack[-1] == "[" and b == "]":
                    stack.pop()
                    count -= 1
                else:
                    return False  # 만약 닫을 수 없는 괄호가 들어오면 False 반환
        return count == 0  # 순회가 끝나고 모든 괄호가 닫혀있으면 True

# Dictionary 사용


class Solution:
    def isValid(self, s: str) -> bool:
        # 닫는 괄호를 키로지정해 여는 괄호타입에 접근가능
        close_brakets = {")": "(", "}": "{", "]": "["}
        stack = []
        count = 0
        for b in s:  # 괄호를 순회하면서
            if b in close_brakets:  # 닫는 괄호라면
                if not stack:  # 스택이 비어있다면 False
                    return False
                # 닫을 수 있는 괄호라면 닫고 스택에서 제거
                if close_brakets[b] == stack[-1]:  # 닫는 괄호를 키로 여는괄호에 접근하여 스택의 Top와 비교
                    stack.pop()
                    count -= 1
                else:
                    return False  # 만약 닫을 수 없는 괄호가 들어오면 False 반환
            else:  # 여는 괄호라면 그냥 스택에 삽입
                stack.append(b)
                count += 1
        return count == 0  # 순회가 끝나고 모든 괄호가 닫혀있으면 True
