# 문제 정의

다음의 기능을 제공하는 해시맵을 디자인하라.

- put(key, value): 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.

- get(key): 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.

- remove(key): 키에 해당하는 키, 값을 해시맵에서 삭제한다.

```python
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
```