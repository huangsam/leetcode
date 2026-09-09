# https://leetcode.com/problems/unique-binary-search-trees/


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Given integer n, return the number of unique BSTs which
        has exactly unique values 1..n.

        Define the recurrence relation as follows:
        - f(n) is the number of unique BSTs with n nodes
        - f(n) = sum[i, 1..n] f(i-1) * f(n-i)
        - where f(0) and f(1) are both 1

        Complexity:
        - Time: O(n^2)
        - Space: O(n)
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                dp[nodes] += dp[left] * dp[right]

        return dp[n]
