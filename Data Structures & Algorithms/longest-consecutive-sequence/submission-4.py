class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prevNum = nums[0]
        counter = 1
        maxVal = 1
      
        for num in nums:
            if num == prevNum:
                continue
            if num == prevNum + 1:
                counter += 1
                maxVal = max(counter, maxVal)
                prevNum = num
            else:
                counter = 1
                prevNum = num
        
        return maxVal
