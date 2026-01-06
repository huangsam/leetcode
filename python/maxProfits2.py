# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit from buying and selling stock multiple times.

        Complexity:
        - Time: O(n)
        - Space: O(1)

        On each day, you may decide to buy and/or sell the stock. You can
        only hold at most one share of the stock at any time. However, you
        can buy it then immediately sell it on the same day.

        Find and return the maximum profit you can achieve.

        Approach:
        - Handle base cases of empty prices and one price
        - Calculate profit whenever stock drops
        - Calculate leftover profits at the very end
        """
        # Handle base cases appropriately
        if len(prices) <= 1:
            return 0

        total_profit = 0
        min_at = 0
        cur_at = 1

        while cur_at < len(prices):
            prev_at = cur_at - 1

            # Calculate profit only when stock drops since it's better
            # to hold when stock rises
            if prices[cur_at] < prices[prev_at]:
                total_profit += prices[prev_at] - prices[min_at]
                min_at = cur_at

            # Find least price possible. The order of conditionals
            # matter in this case. If we flipped this, then we might
            # get the minimum price at the expense of profits. Think
            # of [2,4,1] as an example
            elif prices[cur_at] <= prices[min_at]:
                min_at = cur_at

            cur_at += 1

        # Handle leftover profits. This is especially useful
        # for cases like [1..10], where the while loop holds
        # profit indefinitely
        return total_profit + max(prices[cur_at - 1] - prices[min_at], 0)
