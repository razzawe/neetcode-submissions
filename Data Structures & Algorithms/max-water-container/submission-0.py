class Solution:
    def maxArea(self, heights: List[int]) -> int:
       # Need to find second largest height and return secondLargest^2
        res = 0
        j = len(heights) - 1 
        i = 0
        while i < j:
            size = (j-i) * min(heights[i], heights[j])
            res = max(size, res)
            if heights[i] <= heights[j]:
                i += 1
            elif heights[j] <= heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        return res

