class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)] # O(V)
        for v1, v2 in edges: #O(2E) = O(E)
            graph[v1].append(v2)
            graph[v2].append(v1)

        
        visited = set()
        def dfs(v):
            if v in visited:
                return

            visited.add(v)

            for nei in graph[v]:
                dfs(nei)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count

           


    
    # 0: [1]
    # 1: [2, 0]
    # 3: [4]