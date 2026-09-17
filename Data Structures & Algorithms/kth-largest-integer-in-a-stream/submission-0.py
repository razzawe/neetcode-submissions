class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.newHeap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.newHeap, num)
        while len(self.newHeap) > self.k:
            heapq.heappop(self.newHeap)

    def add(self, val: int) -> int:
        res = 0
        heapq.heappush(self.newHeap, val)
        while len(self.newHeap) > self.k:
            heapq.heappop(self.newHeap)
        return self.newHeap[0]
    


        
