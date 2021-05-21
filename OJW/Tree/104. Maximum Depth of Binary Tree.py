
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
