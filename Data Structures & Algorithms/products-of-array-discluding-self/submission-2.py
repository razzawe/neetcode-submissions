class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need product of left side and product of right side

        #prefix and suffix array

        #i.e. nums = [1,2,3]
        #prefix: i.
        pref = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pref[i] = 1 #i = 0: pref = [1]
                continue
            pref[i] = pref[i-1] * nums[i-1] #i = 1: pref = [1, 1*1] #i = 2: pre = [1,1,2]

        #suffix:
        # i.e. nums = [1,2,3]
        suff = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                suff[i] = 1
                continue
            suff[i] = suff[i+1] * nums[i+1] 
        

        for i in range(len(nums)):
            nums[i] = pref[i] * suff[i]
        

        return nums

