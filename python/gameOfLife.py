# https://leetcode.com/problems/game-of-life/

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Given the current board state of the game, update it to the next state.

        The rules of the game are as follows:

        1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
        2. Any live cell with two or three live neighbors lives on to the next generation.
        3. Any live cell with more than three live neighbors dies, as if by over-population.
        4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

        Use bit manipulation: store the next state in the second bit (shifted left by 1), while
        keeping the current state in the least significant bit.
        In the first pass, compute the next state and encode it.
        In the second pass, shift right to get the next state.

        Complexity:
        - Time: O(m * n), where m is the number of rows and n is the number of columns in the board.
        - Space: O(1), in-place update using bit encoding.
        """
        # First pass: compute next state and encode
        for i, row in enumerate(board):
            for j in range(len(row)):
                next_state = self._getNextState(board, i, j)
                board[i][j] = (next_state << 1) | (board[i][j] & 1)

        # Second pass: update to next state
        for i, row in enumerate(board):
            for j in range(len(row)):
                board[i][j] >>= 1

    def _getNextState(self, board: List[List[int]], row: int, col: int) -> int:
        # Get current state using LSB
        current = board[row][col] & 1

        # Calculate the number of live neighbors using LSB
        neighbor_live_count = 0
        for rd in (-1, 0, 1):
            for cd in (-1, 0, 1):
                if rd == 0 and cd == 0:
                    continue
                row_adj = row + rd
                col_adj = col + cd
                row_invalid = row_adj < 0 or row_adj >= len(board)
                col_invalid = col_adj < 0 or col_adj >= len(board[0])
                if row_invalid or col_invalid:
                    continue
                if (board[row_adj][col_adj] & 1) == 1:
                    neighbor_live_count += 1

        if current == 1:
            # Apply rule 1 or 3
            if neighbor_live_count < 2 or neighbor_live_count > 3:
                return 0
            else:
                return 1
        else:
            # Apply rule 4
            if neighbor_live_count == 3:
                return 1
            else:
                return 0
