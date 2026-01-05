# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time: O(m * n)
        Space: O(1)

        Start at (0,0), go right until you hit the end.
        then you go down until you hit the end. Then you
        go left until you hit the end. Then you go up until
        you hit previously marked items. Then you hit the
        right hand side.

        Keep repeating this process until all items in the matrix
        are visited. That means the current direction is exhausted
        and the next direction cannot be traversed.

        Note that r=right, d=down, l=left, u=up.
        """
        # Boolean flags to keep us sane
        visited = [[False] * self._width(matrix) for _ in range(self._height(matrix))]

        # The final result
        result = []

        # The current direction that we are taking
        direction = "r"

        # The current cell that we are on
        x, y = 0, 0

        while True:
            # Add current cell value to result (do-while)
            result.append(matrix[x][y])

            # Mark node as visited (do-while)
            visited[x][y] = True

            # Change direction as needed
            direction = self._nextDirection(matrix, visited, direction, x, y)

            # If direction changed but still cannot proceed, then
            # it's time to circuit break
            if not self._canMove(matrix, visited, direction, x, y):
                break

            # Continue to traverse based on current direction
            if direction == "r":
                y += 1
            elif direction == "d":
                x += 1
            elif direction == "l":
                y -= 1
            elif direction == "u":
                x -= 1

        return result

    def _nextDirection(self, matrix, visited, direction, x, y) -> str:
        next_direction = {"r": "d", "d": "l", "l": "u", "u": "r"}
        if self._canMove(matrix, visited, direction, x, y):
            return direction
        else:
            return next_direction[direction]

    def _canMove(self, matrix, visited, direction, x, y) -> bool:
        if direction == "r":
            if y == self._width(matrix) - 1 or visited[x][y + 1]:
                return False
        elif direction == "d":
            if x == self._height(matrix) - 1 or visited[x + 1][y]:
                return False
        elif direction == "l":
            if y == 0 or visited[x][y - 1]:
                return False
        elif direction == "u":
            if x == 0 or visited[x - 1][y]:
                return False
        return True

    def _width(self, matrix) -> int:
        return len(matrix[0])

    def _height(self, matrix) -> int:
        return len(matrix)
