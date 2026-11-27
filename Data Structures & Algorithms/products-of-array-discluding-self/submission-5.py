class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums) 

        for i in range(len(nums)): #build prefix array
            if i == 0:
                pref[i] = 1
            else:
                pref[i] = pref[i-1] * nums[i-1] # sets pref@index i to value of ongoing prefix's

        for i in range(len(nums)):
            n = len(nums) - 1 #last element 
            if i == 0:
                suff[n] = 1
            else:
                suff[n-i] = suff[n-i+1] * nums[n-i+1]
        
        res = [1] * len(nums)

        for i in range(len(nums)):
    
            res[i] = pref[i] * suff[i]
        
        return res




         
            

