# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        values = list()
        
        node = head
        
        while node:
            values.append(node.val)
            node = node.next
            
        values.sort()
        
        sorted_head = ListNode(values[0], None)
        sorted_node = sorted_head
        
        for i in range(1, len(values)):
            sorted_node.next = ListNode(values[i], None)
            sorted_node = sorted_node.next
            
        return sorted_head