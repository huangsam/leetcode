# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)

        You want to maximize your profit by choosing a single
        day to buy one stock and choosing a different day in
        the future to sell that stock.

        Return the maximum profit you can achieve from
        this transaction. If you cannot achieve any
        profit, return 0.

        prices = [7,1,5,3,6,4]
        output = 5

        Approach:
        - Look for smallest value for future days
        - If the current price is <= prev, update smallest
        - If the current price is > prev, calculate profit
        - Return the best positive profit you can find
        """
        if len(prices) < 1:
            raise ValueError("Got non-empty list of prices")
        max_profit = 0
        min_price_so_far = prices[0]
        for price in prices:
            if price <= min_price_so_far:
                min_price_so_far = price
            else:
                current_profit = price - min_price_so_far
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
