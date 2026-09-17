class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = zip(position, speed)
        reversePairs = sorted(pairs, reverse=True)
        times = []
        # maxTime = (target - reversePairs[0][0]) / reversePairs[0][1]
        # for i in range(len(position)):
            # curTime = (target - reversePairs[i][0]) / reversePairs[i][1]
            # if curTime > maxTime or len(times) == 0:
            #     times.append(curTime)
            #     maxTime = curTime
        
        # return len(times)
        
        for p, s in reversePairs:
            times.append((target - p) / s)
            if len(times) >=2 and times[-1] <= times[-2]:
                times.pop()
        return len(times)



            
     