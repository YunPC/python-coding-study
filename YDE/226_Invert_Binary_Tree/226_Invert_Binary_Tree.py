# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None:
            
            return root
        
        queue = []
        
        queue.append(root)
        
        while queue:
            
            node = queue.pop(0)
            
            temp_node = node.left
            node.left = node.right
            node.right = temp_node
            
            if node.left is not None:
                
                queue.append(node.left)
            
            if node.right is not None:
                
                queue.append(node.right)
            
        return root