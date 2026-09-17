class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check if cycle, all nodes reachable, len(edges) == n -1
        
        # check edges == n-1.
        if len(edges) != n-1:
            return False

        # initiate undirected graph.
        graph = [[] for _ in range(n)]
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # check cycles.
        visited = set()
        def dfs(v, parent):
            if v in visited:
                return False
                
            visited.add(v)
            for nei in graph[v]:
                if nei == parent:
                    continue
                if not dfs(nei, v):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n #checking if visited all nodes
        
        