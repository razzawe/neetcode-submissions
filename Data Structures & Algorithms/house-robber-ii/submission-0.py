class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1])) #check excluding 1 as well as excluding last place, choose the max between the two

    
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        #nums: [2,3,2]
        #dp: [2,3,0]
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2]) #skip current house and keep current most robbed or rob current house
        
        return dp[-1]