# 형변환 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = ''
        l2_num = ''
        while l1:
            l1_num += str(l1.val)
            l1 = l1.next
        while l2:
            l2_num += str(l2.val)
            l2 = l2.next
        l_sum = (str(int(l1_num[::-1])+int(l2_num[::-1])))[::-1]
        s_node = ListNode(l_sum[0])
        target = s_node
        for i in range(1, len(l_sum)):
            target.next = ListNode(l_sum[i])
            target = target.next
        return s_node

# 나눗셈 풀이


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = 0
        l2_num = 0
        i = 1
        while l1:
            l1_num += l1.val * (10 ** i)//10
            l1 = l1.next
            i += 1
        i = 1
        while l2:
            l2_num += l2.val * (10 ** i)//10
            l2 = l2.next
            i += 1
        l_sum = l1_num+l2_num
        l_sum, l_mod = divmod(l_sum, 10)
        s_node = ListNode(l_mod)
        target = s_node
        while 0 < l_sum:
            l_sum, l_mod = divmod(l_sum, 10)
            target.next = ListNode(l_mod)
            target = target.next
        return s_node
