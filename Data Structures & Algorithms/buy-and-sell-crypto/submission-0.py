class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        bestProfit = 0
        l= 0
        for r in range(1, n):
            if prices[r] < prices[l]:
                l = r
            bestProfit = max(bestProfit, prices[r] - prices[l])

        return bestProfit