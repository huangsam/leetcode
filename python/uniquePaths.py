# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time: O(m * n)
        Space: O(m * n)
        """
        # Initialize memo array
        memo = [[0] * n for _ in range(m)]

        # Go through each row, m-1 --> 0
        for r in range(m - 1, -1, -1):
            # Go through each col, n-1 --> 0
            for c in range(n - 1, -1, -1):
                # Base case -> at the end
                if r == m - 1 and c == n - 1:
                    memo[r][c] = 1
                # Can go down
                if r + 1 < m:
                    memo[r][c] += memo[r + 1][c]
                # Can go right
                if c + 1 < n:
                    memo[r][c] += memo[r][c + 1]

        # Solve original problem --> starting point = (0,0)
        return memo[0][0]
