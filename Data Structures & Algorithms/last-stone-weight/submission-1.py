class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = 0
        #create max-heap:
        maxHeap = []
        
        for stone in stones:
            heapq.heappush(maxHeap, -1*stone)
        while len(maxHeap) > 1:
                
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)
            if y < x:
                heapq.heappush(maxHeap, -1 * (x-y))
            
        return (maxHeap[0] * -1) if len(maxHeap) == 1 else 0