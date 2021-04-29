# 코스 스케줄

> 코스의 총 개수와 하나의 코스를 완료하기 위해 완료해야 하는 코스 쌍을 담은 배열을 입력받아 모든 코스가 수강 가능한지 확인하여 불리언값을 반환한다.
> 예를들어 `2, [[1,0]]`와 같은 값을 입력받았다면 총 2개의 코스(0, 1)이 있으며 1을 완료하기 위해서는 0을 먼저 완료해야 한다는 뜻이다. 이는 그냥 순서대로 수강하면 되기 때문에 True이다. 하지만 `2, [[1,0],[0,1]]`와 같은 값을 입력받는다면 1을 완료하기 위해서는 0을 완료해야하며 0을 완료하기 위해서는 1을 완료해야 한다는 뜻이다. 이는 논리적으로 불가능 하기 때문에 False이다.

문제를 고민해본 결과 단방향 그래프로 표현하여 하나의 코스를 완료하면 새롭게 진행할 수 있는 코스로 이동하고 다시 해당 코스를 완료하면 다음 코스로 이동할 수 있는지 확인하면 되는 것 같다. 문제는 논리적으로 불가능한 경우를 찾는 것인데, 서로가 서로를 의존하는 형태이면 논리적으로 불가능하다. 이는 그래프에서 사이클이 일어난 경우와 같다.

즉 해당문제는 단방향 그래프에서 시작버텍스를 포함하는 사이클이 존재하는지 찾는 문제로 파악된다.

접근은 그래프의 모든 버텍스를 DFS검색하다 시작 버텍스에 접근하게 된다면 종료하게 만들었다.

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        scheduls = [list() for _ in range(numCourses)]
        # 코스의 갯수만큼 리스트를 만든다

        for to_i, from_i in prerequisites:
            scheduls[from_i].append(to_i)
            # 해당 코스를 완료하면 진행할 수 있는 코스의 번호를 리스트에 넣는다.

        def dfs(self_i, stack):
            while stack:
                target_i = stack.pop()
                visit.add(target_i) # 그래프 내에서 탐색중에 사이클이 발생할 수도 있기 때문에 visit을 추가한다.
                for to_i in scheduls[target_i]:
                    if to_i == self_i: # 만약 순회할 버텍스가 첫번째 버텍스랑 같다면 사이클이 발생하는 그래프
                        return False
                    elif to_i in visit:
                        continue
                    else:
                        stack.append(to_i)
            return True

        for i in range(numCourses):
            visit = set()
            if not dfs(i, [i]):
                return False
        return True
```

이렇게 풀이를 했는데, `588ms`가 걸렸다. 릿코드에서도 상당히 느리다고 알려줬다. 순회를 하지 않는게 확정인 경우에는 첫번째 반복문에서 dfs를 생략하는 게 성능에 좋을 것 같다. 고민을 하다가 책을 봤는데, 책에서는 재귀함수를 이용해서 코드를 다시 짜서 생각해야 한다. 그래서 그냥 다른 방법을 생각해봤다.

그래서 다음과 같이 is_skip이라는 set을 추가해서 만약 해당 버텍스를 포함해서 순회했을 때 아무런 이상이 없다면 유지되게 만들었다. 그런데 만약 탐색중 사이클이 발생하는 경우라면 그래프 사이클이 의심되기 때문에 해당 버텍스는 제거한다.

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        scheduls = [list() for _ in range(numCourses)]
        is_skip = set()

        for to_i, from_i in prerequisites:
            scheduls[from_i].append(to_i)

        def dfs(self_i, stack):
            while stack:
                target_i = stack.pop()
                visit.add(target_i)
                for to_i in scheduls[target_i]:
                    is_skip.add(to_i)
                    if to_i == self_i:
                        return False
                    elif to_i in visit:
                        is_skip.remove(to_i)
                        continue
                    else:
                        stack.append(to_i)
            return True

        for i in range(numCourses):
            visit = set()
            if i in is_skip:
                continue
            if not dfs(i, [i]):
                return False
        return True
```

이렇게 푸니 `112ms`로 시간을 줄일 수 있었으나 이 역시 느린 풀이이다. 릿코드에서 다른 풀이를 가져와 봤다.

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = defaultdict(list)
        deg = [0]*numCourses

        for course,pre in prerequisites:
            m[pre].append(course)
            deg[course] += 1
            # 완료해야 하는 코스의 갯수도 함께 저장한다.

        queue = []

        for i in range(numCourses):
            if deg[i] == 0:
                queue.append(i)
        # 바로 완료할 수 있는 코스를 저장

        if len(queue) == 0:
            return False
        # 바로 완료할 수 있는 코스가 하나도 없다면 불가능

        for i in queue:
            # 바로 완료할 수 있는 코스를 찾아
            for num in m[i]:
                # 해당 코스를 완료한 뒤 완료할 수 있는 코스에 접근
                deg[num] -= 1
                # 해당 코스의 선행 코스를 하나 제거
                if deg[num] == 0:
                    # 만약 제거했을 때 선행 코스가 없다면
                    queue.append(num)
                    # 바로 완료할 수 있는 큐에 추가
        return len(queue) == numCourses
        # 큐의 갯수가 코스의 갯수와 같다면 결국 모든 코스를 해결할 수 있다는 의미
```

100% 이해는 되지 않지만, DFS, BFS가 아닌 선행조건의 갯수를 설정하고 차감하는 방법으로 진행했다. 신박하다.
