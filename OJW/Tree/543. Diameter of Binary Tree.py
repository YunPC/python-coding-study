class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        answer = 0

        def recur(node):
            nonlocal answer

            if not node:
                return 0

            left = recur(node.left)
            right = recur(node.right)

            answer = max(answer, left + right)
            return max(left, right) + 1

        recur(root)
        return answer
