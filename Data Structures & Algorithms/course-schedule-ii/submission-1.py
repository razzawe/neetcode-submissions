class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #return order to take to finish all courses 
        #if cycle, return [] OR 

        res = []
        # create graph of course -> prerequisites
        preqMap = [[] for _ in range(numCourses)] # O(V) (creating prereq map for all vertices (courses))
        for crs, preq in prerequisites: # E relationships, so O(E)
            preqMap[crs].append(preq) 

        #So, O(V+E) for creating graph of course -> prerequs


        # first, check if there are any cycles. 
        visited = set() #checked courses
        visiting = set() #currently traversing through. 
        def dfs(crs):
            if (crs) in visiting: #implies theres a cycle (O(1))
                return False
            if (crs) in visited: #implies already checked for cycle and is valid (O(1))
                return True
            visiting.add(crs)
            for preq in preqMap[crs]: #checking all prerequisites to see if they have any cycles (deg(crs1) + deg(crs2)...+deg(crsn) = E)
                if not dfs(preq): #O(deg(crs_i)), where i is some course i...n
                    return False
                
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        


        for i in range(numCourses): # O(V), visit V courses
            if not dfs(i): #O(deg(i)), visiting E courses total
                return []
        #So, outer loop is O(V) for visiting each course, and inner loop is O(E) for checking all prereqs for all courses (V) total. Hence, O(V+E)

        #Total, we have O(2V + 2E) = O(V+E)
        return res

