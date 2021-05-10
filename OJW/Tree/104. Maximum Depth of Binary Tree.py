# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        answer = -1

        def recur(node, depth):
            nonlocal answer

            if node is None:
                answer = max(answer, depth)
                return

            recur(node.left, depth + 1)
            recur(node.right, depth + 1)

        recur(root, 0)

        return answer
