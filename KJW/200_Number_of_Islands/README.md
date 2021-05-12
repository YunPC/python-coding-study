# 섬의 개수

> 0과 1로 이루어진 2차원 배열을 받아 해당 2차원 배열 내에서 섬으로 이루어진 부분을 찾아 개수를 출력한다.
> 예를 들어 다음과 같은 배열이 있다면 상하좌우가 1로 연결된 부분을 섬으로 처리하여 총 3을 출력한다.
> [
> ["1","1","0","0","0"],
> ["1","1","0","0","0"],
> ["0","0","1","0","0"],
> ["0","0","0","1","1"]
> ]

DFS혹은 BFS를 통해 1과 연결된 부분들을 모두 체크해 주면 될것 같다. 나는 DFS를 통해 진행했다. 먼저 2차원 배열을 순회하면서 "1"인 부분을 발견하면 DFS를 시작하여 연결된 부분을 모두 "2"로 변경한다. 그리고 순회를 반복한다.

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(stack):
            while stack:
                x, y = stack.pop()
                grid[x][y] = '2' # 방문처리
                # 이후 상하좌우가 2차원 배열의 범위 안에 있고 값이 '1'이라면 스택에 추가하여 순회할 수 있게 한다.
                if x+1 < len(grid) and grid[x+1][y] == '1':
                    stack.append((x+1, y))
                if x-1 > -1 and grid[x-1][y] == '1':
                    stack.append((x-1, y))
                if y+1 < len(grid[x]) and grid[x][y+1] == '1':
                    stack.append((x, y+1))
                if y-1 > -1 and grid[x][y-1] == '1':
                    stack.append((x, y-1))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1': # 섬이 존재한다면 DFS 시작
                    count += 1 # 섬의 갯수 증가
                    dfs([(i, j)]) # 해당 섬의 시작좌표를 스택으로 전달
        return count
```

이렇게 탐색 좌표를 DFS로 처리하여 문제를 해결하였다.
