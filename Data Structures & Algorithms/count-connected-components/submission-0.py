class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)] # O(V)
        for v1, v2 in edges: #O(2E) = O(E)
            graph[v1].append(v2)
            graph[v2].append(v1)

        count = 0
        visited = set()
        def dfs(v, parent):
            if v in visited and v != parent:
                return

            visited.add(v)

            for nei in graph[v]:
                if nei == parent:
                    continue
                dfs(nei, v)
        
        for i in range(n):
            if i in visited:
                continue
            else:
                count += 1
                dfs(i, -1)
        
        return count

           


    
    # 0: [1]
    # 1: [2, 0]
    # 3: [4]