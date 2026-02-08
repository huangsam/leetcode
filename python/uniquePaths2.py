# https://leetcode.com/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Count unique paths in a grid with obstacles from top-left to bottom-right.

        Use DP: memo[r][c] is ways to end from (r,c).
        If obstacle (1), 0; else, sum from (r+1,c) and (r,c+1).

        Fill from bottom-right: last row and column have 1 if no obstacle and reachable.

        Complexity:
        - Time: O(m * n)
        - Space: O(m * n)
        """
        # Initialize memo array
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]

        # Go through each row, m-1 --> 0
        for r in range(rows - 1, -1, -1):
            # Go through each col, n-1 --> 0
            for c in range(cols - 1, -1, -1):
                # If it's not an obstacle
                if obstacleGrid[r][c] == 0:
                    # Base case -> at the end
                    if r == rows - 1 and c == cols - 1:
                        dp[r][c] = 1
                    # Can go down
                    if r + 1 < rows:
                        dp[r][c] += dp[r + 1][c]
                    # Can go right
                    if c + 1 < cols:
                        dp[r][c] += dp[r][c + 1]

        # Solve original problem --> starting point = (0,0)
        return dp[0][0]
