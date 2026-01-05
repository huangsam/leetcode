# https://leetcode.com/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Time: O(m * n)
        Space: O(m * n)
        """
        # Initialize memo array
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * cols for _ in range(rows)]

        # Go through each row, m-1 --> 0
        for r in range(rows - 1, -1, -1):
            # Go through each col, n-1 --> 0
            for c in range(cols - 1, -1, -1):
                # If it's not an obstacle
                if obstacleGrid[r][c] == 0:
                    # Base case -> at the end
                    if r == rows - 1 and c == cols - 1:
                        memo[r][c] = 1
                    # Can go down
                    if r + 1 < rows:
                        memo[r][c] += memo[r + 1][c]
                    # Can go right
                    if c + 1 < cols:
                        memo[r][c] += memo[r][c + 1]

        # Solve original problem --> starting point = (0,0)
        return memo[0][0]
