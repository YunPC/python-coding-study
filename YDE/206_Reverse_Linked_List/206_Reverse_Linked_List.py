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
