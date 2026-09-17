class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for preq, course in prerequisites: #adjacency list for each course (pre reqs for each course)
            adj[course].append(preq)
        
        # hasCycle:

        visited = set()
        in_stack = set()
        def dfs(node):
            if node in in_stack:
                return True # it is a cycle
            if node in visited:
                return False # it is not a cycle
            visited.add(node)
            in_stack.add(node)    

            for nei in adj[node]:
                if dfs(nei):
                    return True
            in_stack.remove(node)
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
