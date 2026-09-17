class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        minNum = prices[0]
        maxNum = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minNum and i != len(prices)-1:
                minNum = prices[i]
                maxNum = minNum
            elif prices[i] > maxNum:
                maxNum = prices[i]
            
            if maxNum - minNum > profit:
                profit = maxNum - minNum

        return profit