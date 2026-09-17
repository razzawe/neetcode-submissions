"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # do it recursively.
        # recursive function that fully explores a node.
        # if seen[node]:
        # return seen[node]
        # else:
        # instantiate new node
        # 
        cur = head
        seen = {}
        
        newHead = Node(0)
        newCur = newHead

        while cur is not None:  

            # adding new node (or seen from random) to length of new list
            if cur in seen:
                newNode = seen[cur]
            else:
                newNode = Node(cur.val)
                seen[cur] = newNode

            newCur.next = newNode

            # traverse to the new node
            newCur = newCur.next
            
            #set new node value to value in original list
            # newCur.val = cur.val
            
            # check for random + add random (whether seen or not seen)
            if cur.random is None:
                newCur.random = None
       
            elif cur.random in seen:
                newCur.random = seen[cur.random]
            else:
                newRand = Node(cur.random.val)
                newCur.random = newRand
                seen[cur.random] = newRand

            cur = cur.next
        
        return newHead.next




      
        