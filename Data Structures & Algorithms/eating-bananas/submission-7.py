class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            time = 0
            for i in range(len(piles)):
                if piles[i] <= mid:
                    time += 1
                else:
                    time += math.ceil(piles[i] / mid)
            print(time)
            if time > h:
            
                l = mid + 1
            
            
            elif time <= h:
                k = min(k, mid)
                r = mid - 1
          
        return k
