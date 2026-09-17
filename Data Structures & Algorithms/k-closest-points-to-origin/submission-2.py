class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # maintain max-heap so we always pop max element; once you pop until its k size, the smallest k are left over
        heap = []
        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(heap, (-dist, [x, y]))
            while len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            dist, [x,y] = heapq.heappop(heap)
            res.append([x,y])
        
        return res