# https://leetcode.com/problems/sudoku-solver/


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Write a program to solve a Sudoku puzzle by filling the empty cells.

        What we need in order to do this:

        - Row-checker: binary int for one row, for 9 rows
        - Col-checker: binary int for one col, for 9 cols
        - Grid-checker: binary int for one grid, for 9 grids

        Traverse left to right, top to bottom. If one thing needs insertion,
        then replace the "." with a 1-9 and modify the associated binary int
        for row, col, grid. Then undo the num placement and move to the next
        item. If a solution is found, then terminate.
        """
        rows = [0] * 9
        cols = [0] * 9
        grids = [0] * 9

        # Store precomputed (row, col, grid) to avoid function calls
        empty = []

        for r in range(9):
            for c in range(9):
                g = (r // 3) * 3 + (c // 3)
                if board[r][c] == ".":
                    empty.append((r, c, g))
                else:
                    mask = 1 << int(board[r][c])
                    rows[r] |= mask
                    cols[c] |= mask
                    grids[g] |= mask

        def backtrack(idx: int) -> bool:
            if idx == len(empty):
                # By this point in the iteration we are done
                return True

            r, c, g = empty[idx]
            used = rows[r] | cols[c] | grids[g]

            for num in range(1, 10):
                mask = 1 << num
                if not (used & mask):
                    board[r][c] = str(num)
                    rows[r] |= mask
                    cols[c] |= mask
                    grids[g] |= mask

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r] ^= mask
                    cols[c] ^= mask
                    grids[g] ^= mask

            return False

        backtrack(0)
