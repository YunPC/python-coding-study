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
