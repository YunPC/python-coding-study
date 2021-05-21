# Tree

## 1. 104. Maximum Depth of Binary Tree

### 문제 설명

- 이진 트리의 최대 깊이를 찾는 문제.

### 코드

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        answer = -1

        def recur(node, depth):
            nonlocal answer

            if node is None:
                answer = max(answer, depth)
                return

            recur(node.left, depth + 1)
            recur(node.right, depth + 1)

        recur(root, 0)

        return answer

```

### 풀이

#### 1. 개수로 계산하기

- Input 이 배열 형태로 들어온다면, 배열의 개수를 통해 깊이를 알 수 있다. 1,3,7,15,31 순으로 증가하므로 공차가 2n 인 등차수열로 볼 수 있다. 이를 통해 계산하면 1일때 깊이 1, 3까지 깊이 2, 7까지 깊이 3을 계산하면 깊이 구하기가 가능하다.
- 입력 형식이 배열이 아니기 때문에 불가능한 풀이였다.

#### 2. 순회하기

- 재귀 형식으로 순회하면서 최대 깊이를 찾는다. 이 때 인자에 depth 를 넣어주었는데 만약 기존에 선언한 배열에 값을 더하는 방식을 사용하면 계속해서 depth 가 변경되기 때문에 파라미터에서 +1을 한 값을 넘겨주는것이 좋다.

## 2. 543. Diameter of Binary Tree

### 문제 설명

- 가장 긴 노드 간의 거리를 return 하는 문제

### 코드

```python
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        answer = 0
        def recur(node):
            nonlocal answer

            if not node:
                return 0

            left = recur(node.left)
            right = recur(node.right)

            answer = max(answer, left + right)
            return max(left, right) + 1

        recur(root)
        return answer

```

### 풀이

#### 1. 왼쪽 오른쪽의 최대 길이를 더해주기

- node.left 의 최대 길이와 node.right 의 최대길이를 구해서 더해준다. -> wrong answer 발생.

##### 예외 케이스
- 그림을 그려가면서 이해하려고 노력한 결과 만약 루트에서 왼쪽 노드가 없고 오른쪽 노드만 있는 경우가 예외 케이스가 된다.
- 문제 설명에서 **This path may or may not pass through the root.** 라는 설명이 있다. 즉, 루트를 거치지 않았음에도 가장 긴 지름이 나올 수 있다. 1번 풀이의 경우 루트를 항상 거친다는 가정이 들어갔기 때문에 답이 될 수 없다.

#### 2. 노드의 끝에서 상태값 더하기

- 맨 끝(dfs 를 통해 찾는다) 에서 부터, 루트까지의 거리를 찾아나가면서 더한다.
- 먼저 왼쪽 자식 노드의 값들을 찾아 루트까지의 최대 거리를 구해준다.
- 이후 오른쪽 자식 노드의 값들을 찾아 루트까지의 최대 거리를 구해준다.
- 두 값을 더해준다.
- 풀이시에 신기했던 점은, 책에 나와있는 코드는 answer 을 -1 로 두고 left + right + 2 를 해준다.

```python
    if not node:
        return -1

    answer = max(answer, left + right + 2)
```

- 대신 return 0 과 + 2 를 빼주면 놀랍게도 48ms 였던 코드가 36ms 로 바뀐다. 아마 더하기 연산이 눈에 띄게 줄어들었던 점이 속도를 높일 수 있었던 것 같다. 이전에는 다른 코드보다 34% 빨랐지만 이후에 96% 까지 올렸다.

## 3. 687. Longest Univalue Path

### 문제 설명

- 이진 트리의 노드간 최대 지름 길이를 찾는 문제. 2번 문제와 다른점은 노드값이 같은 경우에만 지름 길이를 계산하는 문제이다.

### 코드

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        answer = -1

        def recur(node, depth):
            nonlocal answer

            if node is None:
                answer = max(answer, depth)
                return

            recur(node.left, depth + 1)
            recur(node.right, depth + 1)

        recur(root, 0)

        return answer

```

### 풀이

#### 1. 상태값을 이용하기
- 먼저 dfs 를 통해 왼쪽 맨 마지막 노드부터 시작한다. 만약 부모 노드의 value 값과 같다면 현재 노드의 상태값을 1 더해 준다. 이후 부모 노드로 돌아가면서 왼쪽과 오른쪽 노드의 상태값을 더해주고 최대값을 찾아준다.

## 4. 1038. Binary Search Tree to Greater Sum Tree


### 문제 설명

- BST 에서 노드보다 큰 값들이 있다면 전부 더해준 새로운 트리를 만드는 문제이다.

### 코드

```python
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        value = 0

        def recur(node):
            nonlocal value

            if node is None:
                return

            recur(node.right)
            node.val += value
            value = node.val
            recur(node.left)

        recur(root)
        return root

```

### 풀이

#### 1. 오른쪽 자식부터 순회
- 가장 오른쪽 자식부터 순회하고 (BST 이기 때문에 오른쪽 값이 무조건 크다.) 값을 더해가면서 노드의 val 값을 갱신한다. 따로 recur 를 만들어 주는것 보다, 원래 있는 코드를 재귀 함수처럼 사용하는것이 런타임이 빠르다.
