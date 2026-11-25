# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Find max profit from up to 2 transactions across days. Both must
        be done on completely different days.

        We use a split 1-dp approach where we compute best profit from lhs
        and rhs, then find the max profit by summing the two at the end.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        n = len(prices)
        if n <= 1:
            return 0

        # Best profit from lhs, moving forwards
        left = [0] * n
        # Best profit from rhs, moving backwards
        right = [0] * n

        min_price = 10**5 + 1
        max_price = -1
        max_profit_seen = 0
        for i in range(n):
            min_price = min(prices[i], min_price)
            if i > 0:
                left[i] = max(prices[i] - min_price, left[i - 1])
            max_price = max(prices[n - i - 1], max_price)
            if i > 0:
                right[n - 1 - i] = max(max_price - prices[n - 1 - i], right[n - i])

        for i in range(len(left)):
            max_profit_seen = max(left[i] + right[i], max_profit_seen)

        return max_profit_seen

    def maxProfitState(self, prices: list[int]) -> int:
        """
        We use a state machine approach where we track the best profit
        for each of the 5 states (0, 1, 2, 3, 4) where:
        - 0: no transactions yet
        - 1: first buy
        - 2: first sell
        - 3: second buy
        - 4: second sell

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        s0 = 0
        s1 = -prices[0]
        s2 = float("-inf")
        s3 = float("-inf")
        s4 = float("-inf")

        for price in prices[1:]:
            s1 = max(s1, s0 - price)
            s2 = max(s2, s1 + price)
            s3 = max(s3, s2 - price)
            s4 = max(s4, s3 + price)

        return int(max(s0, s2, s4))
