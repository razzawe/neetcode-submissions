class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        validStarts = set()
        longest = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                validStarts.add(num)
        
        for num in validStarts:
            length = 1
            while num + 1 in numsSet:
                length += 1
                num += 1

            if length > longest:
                longest = length
        return longest