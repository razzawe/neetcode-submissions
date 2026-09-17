class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for crs, preq in prerequisites:
            adjList[crs].append(preq)
            
        visited = set()
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True