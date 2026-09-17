class Node:
    def __init__(self, key=0, value=0, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    # dict and linked list
    # dict has pointers to elements of linked list
    # linked list head will be oldest element (least recently used)
    lru = Node()
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev
            value = self.cache[key].value
            self.cache[key] = self.listIns(key, value)
            return self.cache[key].value
        return -1

    def listIns(self, key: int, value: int) -> Node:
        #[head,tail]
        # marking spot for insertion
        insAt = self.tail.prev
        
        # creating new list node
        newNode = Node()
        newNode.key = key
        newNode.value = value
     

        # inserting new node
        newNode.prev = insAt
        self.tail.prev = newNode
        newNode.next = self.tail
        insAt.next = newNode

        return newNode
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key) #update position 
            self.cache[key].value = value
            return 

        if len(self.cache) == self.capacity:
            self.cache.pop(self.head.next.key) #remove from cache
            self.head.next = self.head.next.next #remove from linked list (least recent at head of list)
            self.head.next.prev = self.head

    
        
        self.cache[key] = self.listIns(key, value)
        return


        
        
        


