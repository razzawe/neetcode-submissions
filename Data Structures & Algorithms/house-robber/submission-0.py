class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        #nums = [1,2,3]
        dp = [0] * len(nums)
        #[0,0,0]
        dp[0] = nums[0]
        #[1,0,0]
        dp[1] = max(nums[0], nums[1])
        #[1,2,0]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            # either skip this house, or rob it and skip the previous house
        return dp[-1]