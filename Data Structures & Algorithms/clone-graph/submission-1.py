"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {} #already searched + fully copied nodes
        def dfs(node):
            if not node:
                return None

            if node in copies:
                return copies[node]
            
            newNode = Node(node.val)
            copies[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            
            return newNode
        return dfs(node) 
            # if node not in copies:
            #     copies[node] = Node(node.val)