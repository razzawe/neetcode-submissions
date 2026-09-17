class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in diffs:
                return [diffs[k], i]
            else:
                diffs[nums[i]] = i
