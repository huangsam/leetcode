# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        
        Complexity:
        - Time: O(1)
        - Space: O(1)

        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each box must contain the digits 1-9 without repetition.
        """
        row_masks = [0] * 9
        col_masks = [0] * 9
        box_masks = [0] * 9

        # Row-major traversal
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c])

                # Check rows
                if (row_masks[r] >> val) & 1:
                    return False
                row_masks[r] |= 1 << val

                # Check columns
                if (col_masks[c] >> val) & 1:
                    return False
                col_masks[c] |= 1 << val

                # Check boxes
                b = (r // 3) * 3 + (c // 3)
                if (box_masks[b] >> val) & 1:
                    return False
                box_masks[b] |= 1 << val

        return True
