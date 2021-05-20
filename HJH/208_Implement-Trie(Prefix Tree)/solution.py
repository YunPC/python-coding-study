class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()


class Trie:

    def __init__(self):
        self.head = Node(None)
        

    def insert(self, word: str) -> None:
        curr = self.head
        
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
            
        curr.child['*'] = True
        

    def search(self, word: str) -> bool:
        curr = self.head
        
        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        
        return '*' in curr.child
    

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        
        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)