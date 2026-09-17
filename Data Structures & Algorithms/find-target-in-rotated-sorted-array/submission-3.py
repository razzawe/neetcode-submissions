class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            #need to split array into its sorted sections


            if nums[l] <= nums[mid]: #if left side is sorted correctly
                if target >= nums[l] and target < nums[mid]: #check if target is in this range
                    r = mid - 1
                else:
                    l = mid + 1
            
            else: #right side sorted correctly
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            # target = 5
            #[5,6,0,1,2,3]
             




            # if target == nums[mid]:
            #     return mid
            # elif target > nums[mid]:
            #     if mid + 1 < len(nums) and nums[mid+1] < target:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # else: #target < num[mid]
            #     if mid - 1 >= 0 and nums[mid-1] > target:
            #         l = mid + 1
            #     else:
            #         r = mid -1

        return -1