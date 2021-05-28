> 오름차순으로 정렬된 배열을 받은 뒤, 균형잡힌 이진 탐색트리로 반환하라

# 문제풀이

배열이 오름차순으로 정렬되어 있기 때문에 기준 왼쪽으로는 작은 수 오른쪽으로는 큰 수이다. 이진탐색의 원리를 이용해서 노드로 생성해 주면 된다.

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bst_make(l, r, arr):
            if r<l:
                return None
            pivot = (l+r) // 2
            return TreeNode(arr[pivot], bst_make(l, pivot-1, arr), bst_make(pivot+1, r, arr))
        return bst_make(0, len(nums)-1, nums)
```

이렇게 하면 배열의 중앙에 기준점을 잡아 노드를 만들고 양쪽에 다시 새로운 기준점을 만들어 노드를 만드는 것을 반복하여 이진 탐색트리를 만들 수 있다.
