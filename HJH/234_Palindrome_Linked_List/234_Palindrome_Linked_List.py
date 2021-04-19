# src: https://leetcode.com/problems/palindrome-linked-list/

from typing import Deque
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return self.__solution2__(head)

    # Runtime 1352 ms / Memory 47.2 MB
    @staticmethod
    def __solution1__(head: ListNode):
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        if len(nodes) % 2 != 0:
            nodes.pop(len(nodes) // 2)

        while nodes:
            first, last = nodes.pop(0), nodes.pop()
            if first.val != last.val:
                return False

        return True

    # Runtime 772 ms / Memory 47.4 MB
    @staticmethod
    def __solution2__(head: ListNode):
        nodes: Deque = collections.deque()
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        while len(nodes) > 1:
            first, last = nodes.popleft(), nodes.pop()

            if first.val != last.val:
                return False

        return True
