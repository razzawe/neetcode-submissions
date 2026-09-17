class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #return order to take to finish all courses 
        #if cycle, return [] OR 

        res = []
        # create graph of course -> prerequisites
        preqMap = [[] for _ in range(numCourses)]
        for crs, preq in prerequisites:
            preqMap[crs].append(preq)

        # first, check if there are any cycles. 
        visited = set() #checked courses
        visiting = set() #currently traversing through. 
        def dfs(crs):
            if (crs) in visiting: #implies theres a cycle
                return False
            if (crs) in visited: #implies already checked for cycle and is valid
                return True
            visiting.add(crs)
            for preq in preqMap[crs]: #checking all prerequisites to see if they have any cycles
                if not dfs(preq):
                    return False
                
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

