# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Return the fewest number of coins to make up the given amount, or -1
        if it's not possible.

        1-D DP solution where we compare the current coin result with the prior
        results from previous coins. We set the initial value to amount + 1 as
        a sentinel value, which helps us check if the amount is reachable or not.

        Complexity:
        - Time: O(n * m), where n is the amount and m is the coins
        - Space: O(n)
        """
        mem = [amount + 1] * (amount + 1)
        mem[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    mem[i] = min(mem[i], 1 + mem[i - coin])

        return mem[-1] if mem[-1] <= amount else -1
