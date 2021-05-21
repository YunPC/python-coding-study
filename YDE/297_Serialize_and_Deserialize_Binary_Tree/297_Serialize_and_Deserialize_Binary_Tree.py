# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if root is None:
            return ''
        
        queue = []
        res = []
        
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            
            if node is not None:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
                
            else:
                res.append('null')
        
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == '':
            return None
        
        tree = data.split()
        
        queue = []
        
        queue.append((0, TreeNode(tree[0])))
        
        _, root = queue[0]
        
        while queue:
            
            ind, node = queue.pop(0)
            
            left = ind * 2 + 1
            right = ind * 2 + 2
            
            if left < len(tree):
                left_node = TreeNode(tree[left])
                node.left = left_node
                
                queue.append((left, left_node))
                
            if right < len(tree):
                right_node = TreeNode(tree[right])
                node.right = right_node
                
                queue.append((right, right_node))
                
        return root
        
            
            
            
            
            
            
            
            
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))