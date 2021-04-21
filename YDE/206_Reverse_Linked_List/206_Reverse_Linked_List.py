# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime: 36 ms, Memory Usage: 16.3 MB
def solution1(head):
    if head.val is None:
            return ListNode('')
        
    values = []

    while head:
        values.append(head.val)
        head = head.next
        
    list_node = ListNode()    
    start = list_node
    
    for v in values[::-1]:
        start.next = ListNode(v)
        start = start.next
        
    return list_node.next

# Runtime: 28ms, Memory Usage: 20.5MB
def solution2(head):
    def reverse(node, prev=None):
        if not node:
            return prev

        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)