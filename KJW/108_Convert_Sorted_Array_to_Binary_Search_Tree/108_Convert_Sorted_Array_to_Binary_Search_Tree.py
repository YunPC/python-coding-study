from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bst_make(l, r, arr):
            if r < l:
                return None
            pivot = (l+r) // 2
            return TreeNode(arr[pivot], bst_make(l, pivot-1, arr), bst_make(pivot+1, r, arr))
        return bst_make(0, len(nums)-1, nums)
