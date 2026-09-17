class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #pop all mins until the k largest elements are left, then index 0 of array will be kth largest element
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)