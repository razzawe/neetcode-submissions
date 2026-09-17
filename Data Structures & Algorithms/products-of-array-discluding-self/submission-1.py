class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * len(nums)
        prefix = []
        totalprod = 1
        #prefix:
        for i in range(len(nums)):
            curr = nums[i]
            totalprod = totalprod * curr
            prefix.append(totalprod)
        
        totalprod = 1
        #suffix:
        for i in range(len(nums)-1, -1 , -1):
            curr = nums[i]
            totalprod = totalprod * curr
            suffix[i] = totalprod
    
        #newarray:
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix[1]
            elif i == len(nums) - 1:
                res[i] = prefix[len(nums)-2]
            else:    
                res[i] = prefix[i-1] * suffix[i+1]

        return res
       
        
            

            
            


            

