class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) 
        #nums = [-1,0,2,4,6,8]
        # t = -1
        # mid = 2, arr[mid] = 2 so... r = 2, l = 0 
        
        while left < right:
            mid = left + ((right - left) // 2)
            print(mid)
            if nums[mid] < target:
                left = mid + 1
                     
            elif nums[mid] >= target:
                right = mid    
            else:
                return left

        return left if (left < len(nums) and nums[left] == target) else -1


