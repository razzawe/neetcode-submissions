class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = zip(position, speed)
        reversePairs = sorted(pairs, reverse=True)
        times = []
        fleets = 0 
        maxTime = (target - reversePairs[0][0]) / reversePairs[0][1]
        print("max time: " + str(maxTime))
        for i in range(len(position)):
            curTime = (target - reversePairs[i][0]) / reversePairs[i][1]
            if curTime > maxTime or len(times) == 0:
                times.append(curTime)
                maxTime = curTime
        
        return len(times)


            
     