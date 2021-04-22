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

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        value = self.q[self.front]
        self.front = (self.front+1) % len(self.q)
        
        self.full = False
        
        return True
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[(self.rear-1)%len(self.q)]

    def isEmpty(self) -> bool:
        return self.front == self.rear and not self.full

    def isFull(self) -> bool:
        return self.full