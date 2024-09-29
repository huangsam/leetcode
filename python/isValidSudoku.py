# https://leetcode.com/problems/valid-sudoku/
from typing import Iterable, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the nine 3 x 3 sub-boxes of the grid must contain
        the digits 1-9 without repetition.

        Solving the rows and columns should be easy.
        Solving the 3x3 boxes might require some more work.

        Note that first list is rows. Second list is columns.

        We can skip validating characters which are dots.
        """
        # Check board rows and columns
        for i in range(9):
            row = (board[i][c] for c in range(9))
            col = (board[r][i] for r in range(9))
            if not self.hasValidEntries(row):
                return False
            elif not self.hasValidEntries(col):
                return False

        # Check board grids
        for i in range(3):
            for j in range(3):
                grid = (board[i * 3 + x][j * 3 + y] for x in range(3) for y in range(3))
                if not self.hasValidEntries(grid):
                    return False

        return True

    def hasValidEntries(self, entries: Iterable[str]) -> bool:
        seen = set()
        for cell in entries:
            if cell == ".":
                continue
            if cell in seen:
                return False
            seen.add(cell)
        return True
