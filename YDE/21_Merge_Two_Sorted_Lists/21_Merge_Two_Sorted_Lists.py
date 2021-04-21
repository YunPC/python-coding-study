# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: 40 ms, Memory Usage: 14.4 MB
def solution1(l1, l2):
    nodes = []
        
    node = l1
    
    while node is not None:
        nodes.append(node.val)
        node = node.next
        
    node = l2
    
    while node is not None:
        nodes.append(node.val)
        node = node.next
        
    if len(nodes) == 0:
        return ListNode('')
    
    nodes.sort()
    
    list_node = ListNode(nodes[0])
    
    head = list_node
    
    for i in range(1, len(nodes)):
        head.next = ListNode(nodes[i])
        head = head.next
        
    return list_node
