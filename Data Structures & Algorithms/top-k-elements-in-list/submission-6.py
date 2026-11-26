class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)



        min_heap = []
        for num in freq:
            heapq.heappush(min_heap,(freq[num],num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res
           
        
    