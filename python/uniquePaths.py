# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize memo array
        memo = [[0] * n for i in range(m)]

        # go through each row, m-1 --> 0
        for r in range(m - 1, -1, -1):
            # go through each col, n-1 --> 0
            for c in range(n - 1, -1, -1):
                # base case -> at the end
                if r == m - 1 and c == n - 1:
                    memo[r][c] = 1
                # can go down
                if r + 1 < m:
                    memo[r][c] += memo[r + 1][c]
                # can go right
                if c + 1 < n:
                    memo[r][c] += memo[r][c + 1]

        # solve original problem --> starting point = (0,0)
        return memo[0][0]
