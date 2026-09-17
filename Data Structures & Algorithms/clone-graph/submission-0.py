"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}
        
        def dfs(node): 
            if node in copies:
                return copies[node] # if node already explored and defined in copies.

            #if node hasnt already been explored, add it to dictionary and explore:
            newNode = Node(node.val) 
            copies[node] = newNode
            
            for nei in node.neighbors: 
                newNode.neighbors.append(dfs(nei))
            return newNode
        
        return dfs(node) if node else None



# Start with parent node
# Traverse through parent nodes neighbours

                    
