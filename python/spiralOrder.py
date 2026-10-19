# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        Return all elements of a matrix in spiral order.

        For an M x N matrix, where M is the row count and N is the column count,
        we would want to do the following:

        - Start at (0, 0) and go to the (0, N-1), then the top shrinks by 1
        - Go down to the bottom (M-1, N-1), the the right shrinks by 1
        - Go to the left (M-1, 0), then the bottom shrinks by 1
        - Once we go up to (1, 0), we enter a subproblem and shrink left by 1
        - Keep repeating these steps until the top/bottom or left/right overlap

        Complexity:
        - Time: O(m * n)
        - Space: O(1) extra, excluding the output list
        """
        result: list[int] = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for y in range(left, right + 1):
                result.append(matrix[top][y])
            top += 1

            for x in range(top, bottom + 1):
                result.append(matrix[x][right])
            right -= 1

            # Guard against re-walking a row/column when one is left
            if top <= bottom:
                for y in range(right, left - 1, -1):
                    result.append(matrix[bottom][y])
                bottom -= 1

            if left <= right:
                for x in range(bottom, top - 1, -1):
                    result.append(matrix[x][left])
                left += 1

        return result
