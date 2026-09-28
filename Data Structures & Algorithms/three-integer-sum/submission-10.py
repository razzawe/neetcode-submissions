class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        res = []
        if len(nums) == 0:
            return []
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                elif nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        return res