class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi, l, r = 0, 0, 0
        while r <= (len(prices) - 1): 
            if (prices[r] - prices[l] >= maxi):
                maxi = prices[r] - prices[l]
            elif prices[r] < prices[l]:
                l = r
            r += 1

        return maxi

