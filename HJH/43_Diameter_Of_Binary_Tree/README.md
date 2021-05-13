## 풀이

### 43_Diameter_Of_Binary_Tree - 허재혁
> [https://leetcode.com/problems/diameter-of-binary-tree/](https://leetcode.com/problems/diameter-of-binary-tree/)

> 이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.

**나의 풀이**
```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_length = 0
        
        def dfs(node):
            nonlocal max_length
            
            if node is None:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
                
            max_length = max([max_length, left_depth + right_depth])
            return max(left_depth, right_depth) + 1
            
        dfs(root)
        
        return max_length
```
- dfs 문제다.
- left_depth는 왼쪽 subtree의 root의 왼쪽 자식 depth, right_depth는 오른쪽 subtree의 root의 오른쪽 자식 depth로 설정한다.
- leat_node인 경우, 깊이 0을 리턴한다.
- max_length는 left_depth와 right_depth를 더한 값과 기존의 max_length 중 큰 값으로 업데이트한다.
- 마지막 리턴문은 왼쪽 자식의 깊이와 오른쪽 자식의 깊이 중 큰 값에 자신부터 자식들간의 거리인 1을 더해주어 리턴하는 것이다.
