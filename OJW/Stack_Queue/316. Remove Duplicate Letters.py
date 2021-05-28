class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Count(s), []

        for char in s:
            # 일단 문자를 꺼냈기 때문에 counter 를 -1 해준다.
            count[char] -= 1

            # 만약 문자가 스택에 존재한다면, 다음 문자를 탐색하도록 한다.
            # 즉, 스택에 들어있다면 더이상 비교하지 않아도 된다라는 가정이 확실한 사실이 되도록 아래 코드를 잘 짜야한다.
            if char in stack:
                continue

            # 0. 스택에 값이 존재한다면
            # 1. 문자가 1개도 없는 경우 (중복이 없는 경우) 에는 문자를 지울 수 없다. 즉 counter 가 0 보다 커야만 지울 수 있다.
            # 2. 0, 1 을 만족하는 경우에 만약 스택의 마지막 원소가 새로 비교할 char 보다 큰 경우 (문자에서의 순서를 말한다.)
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                stack.pop()

            # 반복문의 밖에서 append 를 해주는 이유는,
            # 1. 위에서 continue 를 사용해서 원하지 않는 문자의 처리가 가능하다.
            # 2. 만약 stack 에 값이 존재하지 않는다고 해서 append 를 하지 않을 수는 없다.
            stack.append(char)

        # 리스트의 문자를 합치는 경우에는 join 을 쓰는것이 효율적이다.
        return "".join(stack)
