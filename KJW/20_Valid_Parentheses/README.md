# 20. Valid Parentheses

> 괄호로 이루어진 문자열을 받아 문자열 내의 모든 괄호가 유효한 지 확인하는 문제

아래의 조건이 있는데,

1. 열린 괄호는 반드시 같은 타입의 괄호로 닫혀야 한다
2. 마지막으로 열린 괄호부터 닫혀야 한다

스택문제라서 그런지 역시 스택의 기운이 물씬 느껴진다. 그런데 문제에 모든 괄호가 유효해야 하는지 유효한 괄호를 포함하면 되는지에 대한 이야기가 없다. 일단은 모든 괄호가 유효해야 한다는 가정으로 문제를 풀기로 했다

```python
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
                if not stack: # 스택이 비어있다면 False
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
        return count == 0 # 순회가 끝나고 모든 괄호가 닫혀있으면 True
```

괄호로 이루어진 문자열을 순회하면서 괄호가 닫히게 되면 스택에서 제거하고 한 번이라도 조건을 어기게 되는 경우가 발생하면 바로 False를 리턴 시킨다. 순회가 모두 정상적으로 종료되고 열린 괄호가 없으면 True를 리턴한다. False가 되는 조건은 아래와 같다.

- 비어있는 스택에 닫히는 괄호가 들어올 때
- 괄호가 열릴 때 마다 카운트를 증가하고 닫히면 감소시킨 뒤 순회 종료 후 카운트가 0이 아닐 때
- 열린 괄호가 다른 타입의 괄호로 닫힐 때

괄호를 검사할 때 딕셔너리를 통해 코드를 간단히 할 수 있을 것 같다

```python
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
```

그런데 이상하게 속도는 단순 IF문을 사용한 것이 빨랐다.

- 단순 IF문 : `20ms`
- 딕셔너리 : `32ms`
