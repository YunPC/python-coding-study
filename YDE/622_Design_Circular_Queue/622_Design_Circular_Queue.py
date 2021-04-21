# Runtime: 64 ms Memory Usage: 15 MB
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.full = False
        self.front = 0
        self.rear = 0
    
    def enQueue(self, value: int) -> bool:
        if self.front == self.rear and self.full:
            return False
        
        self.q[self.rear] = value
        self.rear = (self.rear+1) % len(self.q)
        
        if self.rear == self.front:
            self.full = True
            
        return True