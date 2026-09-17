class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # dict maintaining tuple of points to its k distance from origin (or other way around?).. list of tuples with k mapping to 
        # heap maintaining 
        dists = defaultdict(list)
        dists_heap = []
    
        for x, y in points: # all points to hashmap + heap; O()
            dist = math.sqrt((x*x) + (y*y))
            dists[dist].append([x,y])
            heapq.heappush(dists_heap, dist)
        
        res = []

        for i in range(k):
            dist = heapq.heappop(dists_heap)
            res.append(dists[dist].pop())

        return res

