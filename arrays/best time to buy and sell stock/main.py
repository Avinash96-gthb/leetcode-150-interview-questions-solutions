class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        max_profit = 0
        while r < len(prices):
            if prices[l]<prices[r]:
                current_profit = prices[r]-prices[l]
                max_profit = max(current_profit,max_profit)
            else:
                l=r
            r+=1
        return max_profit
