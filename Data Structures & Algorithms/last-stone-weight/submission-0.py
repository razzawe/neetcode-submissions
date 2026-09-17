class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newHeap = []
        for stone in stones: #create max-heap
            heapq.heappush(newHeap, -1 * stone)
        
        while len(newHeap) > 1:

            stone1 = heapq.heappop(newHeap) * -1
            stone2 = heapq.heappop(newHeap) * -1
                

            if stone1 > stone2:
                newStone = -1 * (stone1 - stone2)
                heapq.heappush(newHeap, newStone)
        
        
        return (newHeap[0] * -1) if len(newHeap) == 1 else 0



