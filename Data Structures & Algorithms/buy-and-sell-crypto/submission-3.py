class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left pointer that starts at the beginning
        # a right pointer that will iterate through each of the elements
        # a max profit variable which will update based on the profit if there is net positive difference
        l = 0
        maxProfit = 0
        for r in range(len(prices)):
            if prices[r] - prices[l] > 0:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
        
        return maxProfit