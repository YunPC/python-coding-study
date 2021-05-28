# 2. Add Two Numbers

> 두 개의 연결리스트를 받아서 순회하여 나온 숫자의 역순의 숫자를 더한뒤 나온 값을 다시 역순의 연결리스트로 반환하는 문제

```python
입력: l1 = [2,4,3], l2 = [5,6,4]
출력: [7,0,8]
계산 과정: 342 + 465 = 807
```

### 나의 첫 번째 풀이

처음에는 1차원적으로 아래의 단계에 따라 풀이했다

1. 각 노드를 순회하여 문자열로 가져온다
2. 문자열로 가져온 노드를 역순으로 뒤집은 뒤 정수로 형변환 후 더한다
3. 더한 값을 문자열로 바꾼 뒤 순서대로 노드를 생성해 이어준다
4. 생성한 노드를 반환한다

```python
# Definition for singly-linked list.
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
        for i in range(1,len(l_sum)):
            target.next = ListNode(l_sum[i])
            target = target.next
        return s_node
```

정말 말 그대로 1차원적인 풀이.. 적어도 문자열로 변환하는 로직만 제거해 보자

### 문자열 변환 없는 풀이

```python
# Definition for singly-linked list.
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
```

### 교재 풀이 (전가산기)

형변환을 모두 나눗셈과 나머지연산으로 변환했지만.. 성능은 그닥 차이나지 않았다. 마지막으로 교재에 있는 전가산기 풀이를 읽어봤는데 이게 가장 좋은 해결방법이었던 것 같다. 나는 기본적으로 노드를 다 숫자로 변환한 뒤 계산을 하고 다시 노드로 만드는 방법을 생각했는데 노드의 특성을 활용하면서 덧셈과 함께 자리올림도 함께 처리할 수 있었다. 코드는 아래와 같다

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next
```

코드가 훨씬 깔끔하기도 하고 시간도 훨씬 빠르다 노드의 구조를 그대로 활용해서 풀이한 것이 인상적이었다.. 나는 멀었다..

- 형변환 : `76ms`
- 나눗셈 : `72ms`
- 전가산기 : `64ms`
