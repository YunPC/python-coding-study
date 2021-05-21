# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        value = 0

        def recur(node):
            nonlocal value

            if node is None:
                return

            recur(node.right)
            node.val += value
            value = node.val
            recur(node.left)

        recur(root)
        return root
