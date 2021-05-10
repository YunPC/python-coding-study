# Runtime: 376 ms
# Memory Usage: 39.3 MB
class MyHashMap:

    def __init__(self):
        
        self.hashTable = [None]*1000001
        

    def put(self, key: int, value: int) -> None:
        
        self.hashTable[key] = value

    def get(self, key: int) -> int:
        
        if self.hashTable[key] is not None:
            return self.hashTable[key]
        
        return -1
        

    def remove(self, key: int) -> None:
        
        if self.hashTable[key] is not None:
            
            value = self.hashTable[key]
            self.hashTable[key] = None
            return value