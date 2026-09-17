class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        # speeds = list(range(1, max(piles)+1))
        # l, r = 0, len(speeds) - 1
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            time = 0
            for i in range(len(piles)):
                # if piles[i] <= speeds[mid]:
                if piles[i] <= mid:
                    time += 1
                else:
                    # time += math.ceil(piles[i] / speeds[mid])
                    time += math.ceil(piles[i] / mid)
            print(time)
            if time > h:
            
                l = mid + 1
                # mid += 1
            
            elif time <= h:
               
                # k = min(k, speeds[mid])
                k = min(k, mid)
            
                r = mid - 1
                # mid -= 1
        return k
