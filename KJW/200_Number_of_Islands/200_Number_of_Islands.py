from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(stack):
            while stack:
                x, y = stack.pop()
                grid[x][y] = '2'  # 방문처리
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
                if grid[i][j] == '1':  # 섬이 존재한다면 DFS 시작
                    count += 1  # 섬의 갯수 증가
                    dfs([(i, j)])  # 해당 섬의 시작좌표를 스택으로 전달
        return count


print(Solution().numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
