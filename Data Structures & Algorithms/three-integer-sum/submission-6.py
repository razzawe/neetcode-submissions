class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #[-1,0,1,2,-1,-4]
        #Sorted:
        #[-4, -1, -1, 0, 1, 2]
        # -1:
        # 

        #Need: nums[i] + nums[j] + nums[k] == 0
        #Equivalent to: nums[i] == -(nums[j] + nums[k]) OR: -nums[i] == nums[j] + nums[k]
        triplets = []
        nums.sort()
        for i in range(len(nums)): #O(n^2)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i+1 #Leftmost index
            r = len(nums)-1 #Rightmost index
            while l < r: #O(n), our target is nums[i] == -(nums[l] + nums[r])
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    triplets.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicate l values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicate r values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    
        return triplets



