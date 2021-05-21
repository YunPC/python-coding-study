class Node():
    def __init__(self, time, is_slow) -> None:
        self.time = time
        self.is_slow = is_slow
        self.left = None
        self.right = None


def solution(N):
    root = Node(0, False)

    def count_node(node):
        if node.time > N:
            return 0
        add_time = node.time+(2 if node.is_slow else 1)
        node.left = Node(add_time, False)
        node.right = Node(add_time, True)
        return count_node(node.left) + count_node(node.right) + 1
    return count_node(root)
