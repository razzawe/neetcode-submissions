class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        #nums = [-1,0,2,4,6,8]
        # t = -1
        # mid = 2, arr[mid] = 2 so... r = 2, l = 0 
        
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] < target:
                left = mid + 1
                     
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


