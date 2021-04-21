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

# Runtime: 60 ms, Memory Usage: 14.4 MB
def solution2(l1, l2):

    if l1.val == '' and l2.val == '':
            return ListNode('')
    
    list_node = ListNode('')

    head = list_node

    while l1 or l2:
        
        if l1 is None:
            
            if head.val == '':
                head.val = l2.val
            else:
                head.next = ListNode(l2.val)
                head = head.next
            
            l2 = l2.next
            
        elif l2 is None:
            
            if head.val == '':
                head.val = l1.val
            else:
                head.next = ListNode(l1.val)
                head = head.next
            
            l1 = l1.next
            
        else:
            if l1.val <= l2.val:
                
                if head.val == '':
                    head.val = l1.val
                else:
                    head.next = ListNode(l1.val)
                    head = head.next
                    
                l1 = l1.next
                
            else:
                if head.val == '':
                    head.val = l2.val
                else:
                    head.next = ListNode(l2.val)
                    head = head.next
                    
                l2 = l2.next
                    
    return list_node

