class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 #index of left-most element
        r = len(numbers) - 1 #index of right-most element
        while l < r:
            curSum = numbers[l] + numbers[r]
    
            if curSum > target:
                r = r - 1
            elif curSum < target:
                l = l + 1
            else:
                return [l+1, r+1]
        return []

        # [1,2,3,4] target: 3
        #1 + 4 = 5
        #1 + 3 = 4
        #1 + 2 = 4

        # [1,2,3,4,5,6,7] target: 

