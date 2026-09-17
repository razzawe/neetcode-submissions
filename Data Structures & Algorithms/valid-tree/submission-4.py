class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Turn edges into graph:
        graph = [[] for _ in range(n)] # (O(V))
        for v1, v2 in edges: #(O(E)), because its undirected, we append in both directions
            graph[v2].append(v1)
            graph[v1].append(v2)
        # A valid tree has:
       
    
        # - N-1 edges for N nodes.
        if len(edges) != n-1:
            return False
        
        # - No cycles + Nodes which are all reachable.
        visited = set()
        visiting = set()
        
        def dfs(v, parent):
            # if v in visiting:
            #     return False # Can not be a valid tree
            if v in visited:
                return False
            
            visited.add(v)
            for nei in graph[v]: # Check all connected nodes.
                if nei == parent:
                    continue 
                if not dfs(nei, v):
                    return False # Cycle detected

            return True

           

        if not dfs(0, -1):
            return False

        return len(visited) == n #checking if equal number of nodes as reached
        


#      0
#     / \
#    1 - 2
#.    3 - 4

# 0 : [1, 2]
# 1: [2]
# 3: [4]