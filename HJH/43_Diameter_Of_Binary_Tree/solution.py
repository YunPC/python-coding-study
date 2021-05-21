# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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


