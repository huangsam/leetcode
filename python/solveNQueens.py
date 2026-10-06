# https://leetcode.com/problems/n-queens/


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        Solve the N-Queens problem and return all distinct solutions.

        Use cols, diag1, and diag2 sets to track the columns and diagonals as
        sets to check for conflicts in O(1) time, which is more efficient
        than checking O(n) for a 2D board.

        Complexity:
        - Time: O(n!)
        - Space: O(n)
        """
        res: list[list[str]] = []
        puzzle: list[str] = []

        cols: set[int] = set()
        diag1: set[int] = set()
        diag2: set[int] = set()

        def backtrack(row: int) -> None:
            # Base case: fully solved n-queens
            if row == n:
                res.append(puzzle.copy())
                return

            # Recursive case: validate, insert, backtrack, undo
            for col in range(n):
                if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    puzzle.append("." * col + "Q" + "." * (n - col - 1))
                    backtrack(row + 1)
                    puzzle.pop()
                    diag2.remove(row + col)
                    diag1.remove(row - col)
                    cols.remove(col)

        # Run backtrack solution to get the answer
        backtrack(0)

        return res
