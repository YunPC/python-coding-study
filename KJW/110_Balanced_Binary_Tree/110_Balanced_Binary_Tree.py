class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left is False or right is False:
                return False
            if abs(left - right) > 1:
                return False
            return max(left, right) + 1
        result = dfs(root)
        if result is not False and 0 <= result:
            return True
        return False
