class Node:
    def __init__(self, value=0, key=0):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:
    # dict and linked list
    # dict has pointers to elements of linked list
    # linked list head will be oldest element (least recently used)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node() #LRU
        self.tail = Node() #MRU

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value

        return -1
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        prev = self.tail.prev
        node.prev = prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node


    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(value, key)
        self.insert(self.cache[key])

  

        if len(self.cache) > self.capacity:
            self.cache.pop(self.head.next.key)
            self.remove(self.head.next)
            
        
     
        


        
        
        


