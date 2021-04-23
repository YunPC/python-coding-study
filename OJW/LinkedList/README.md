# 24. Swap Nodes in Pairs
## 주의할 점
* Linked List 에 대한 이해가 부족하면 풀기 어려울 수도 있다. 문제 풀이 시간보다 Linked List 를 다시 공부한 시간이 훨 길었다.

## 문제 풀이
* 사실 문제 풀이라고 할 내용도 없다. 노드를 스왑하는 것 보다 값을 스왑하는 것이 더 효율적이라고 생각해 값만 바꿔주고 다음 노드를 2번 이동하는 방식을 통해 구현했다.
* 노드가 홀수개일 경우가 예외 케이스가 되는데, 그냥 안 바꿔주면 그만이다.

```{.python}
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

```

# 328. Odd Even Linked List
## 주의할 점
* 당장 문제 이해를 잘 못 해서 힘들었다. 홀수 다음에는 짝수가 나와야 하는 문제인줄 알고 고생했지만 알고보니 홀수 노드를 이어주고 짝수 노드를 그 뒤에 이어주면 되는 문제였다.

## 문제 풀이
* 문제가 직관적이다. 홀수는 홀수 노드에, 짝수는 짝수 노드에 넣어주고 둘을 이어주기만 하면 그만이다. 대신 Linked List 에 대해 잘 모른다면 역시 힘들 수도 있다.

```{.python}
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        # 홀수 노드를 head
        odd = head
        # 짝수 노드는 head.next 로 먼저 이어준다.
        even = head.next
        # 또 하나의 head 를 선언하는 것은, odd.next 에 붙여주기 위해서다.
        # LinkedList 는 array 와 다르게 index 를 이용한 접근이 불가능하기 때문이다.
        even_head = head.next

        # 1 3 5 7
        # 2 4 6 8
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 이어주기
        odd.next = even_head

        # 노드의 head 를 return
        return head

```
# 92. Reverse Linked List
## 주의할 점
* 그냥 뒤집는 것도 아니고 지정된 인덱스 m 에서 n 까지 뒤집는 문제이다. 
* 주의하고 뭐 할것도 없이 그냥 어렵다. 답지 보고 이해하는 것도 오래 걸리는 문제이다. 만약 다음에 만나게 된다면 절대 틀리지 않을 정도로 외우는게 답이다......... ㅠㅠ

