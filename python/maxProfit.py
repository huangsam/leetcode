# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        alen = len(prices)
        i = 0
        small = 0
        max_profit = 0
        while i < alen:
            if prices[i] < prices[small]:
                small = i
                continue
            current_profit = prices[i] - prices[small]
            if max_profit < current_profit:
                max_profit = current_profit
            i += 1
        return max_profit
