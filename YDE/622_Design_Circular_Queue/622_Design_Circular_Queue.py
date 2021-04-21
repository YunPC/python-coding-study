# Runtime: 64 ms Memory Usage: 15 MB
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.full = False
        self.front = 0
        self.rear = 0
    
    