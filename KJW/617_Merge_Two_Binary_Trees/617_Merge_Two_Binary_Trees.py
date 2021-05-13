class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs(node1, node2):
            if node1 and node2:
                return TreeNode(node1.val+node2.val, dfs(node1.left, node2.left), dfs(node1.right, node2.right))
            if node1 or node2:
                return TreeNode(node1.val if node1 else node2.val,
                                dfs(node1.left if node1 else None,
                                    node2.left if node2 else None),
                                dfs(node1.right if node1 else None, node2.right if node2 else None))
            return None

        return dfs(root1, root2)
