from typing import List
import collections


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        return self.__solve_with_stack(T)
        pass

    # Time Limit Exceeded
    @staticmethod
    def __solve_with_queue(T):
        queue: collections.deque = collections.deque()
        answer = []

        for temperature in T:
            queue.append(temperature)

        while queue:
            popped = queue.popleft()
            interval = 1
            warmer = False

            for rest_temperature in queue:
                if popped < rest_temperature:
                    warmer = True
                    break
                interval += 1

            if warmer:
                answer.append(interval)
            else:
                answer.append(0)

        return answer

    # Runtime 516 ms / Memory 19 MB
    @staticmethod
    def __solve_with_stack(T):
        answer = [0] * len(T)
        stack = []

        for i in range(len(T) - 1, -1, -1):
            print(stack)
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                answer[i] = stack[-1] - i
            stack.append(i)
        return answer


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
