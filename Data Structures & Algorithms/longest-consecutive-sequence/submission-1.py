class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxLength = 0
        for i in range(len(nums)):
            length = 1
            while nums[i] + length in setNums:
                length += 1
            maxLength = max(maxLength, length)
        
        return maxLength