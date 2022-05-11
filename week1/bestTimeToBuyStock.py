from typing import *

# Solution hint : use pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        globalMax = 0
        buy, sell = 0, 1

        while sell < len(prices):

            profit = prices[sell] - prices[buy]

            if profit < 0:
                buy = sell

            sell += 1
            globalMax = max(profit, globalMax)

        return globalMax


solution = Solution()
print("6", solution.maxProfit([1, 2, 3, 4, 5, 6, 7]))
print("5", solution.maxProfit([7, 1, 5, 3, 6, 4]))
print("0", solution.maxProfit([7, 6, 4, 3, 1]))
