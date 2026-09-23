import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy, sell = math.inf, -math.inf
        for p in prices:
            if p < buy:
                buy = p
                sell = -math.inf
            elif p > sell:
                sell = p
            maxProfit = max(maxProfit, sell-buy)
        return maxProfit
