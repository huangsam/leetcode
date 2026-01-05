# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Time: O(n^2)
        Space: O(1)

        Do not return anything, modify matrix in-place instead.

        Observation for 3x3:
            starts at 0,0 -> 0,2 -> 2,2 -> 2,0 (size 3)
            ends at 1,1 due to size 1 (size 1)

        Observation for 4x4:
            starts at 0,0 -> 0,3 -> 3,3 -> 3,0 (size 4)
            starts at 1,1 -> 1,2 -> 2,2 -> 2,1 (size 2)
            ends at 2,2 due to size 0 (size 0)
        """
        size, start = len(matrix), 0
        while size > 1:
            # avoid shuffling the corners twice
            for i in range(size - 1):
                end = start + size - 1
                forward, backward = start + i, end - i

                # store top
                top = matrix[start][forward]

                # top <- left
                matrix[start][forward] = matrix[backward][start]

                # left <- bottom
                matrix[backward][start] = matrix[end][backward]

                # bottom <- right
                matrix[end][backward] = matrix[forward][end]

                # right <- top
                matrix[forward][end] = top

            # decrease size by 2, since N-S-E-W all reduce by 1
            size -= 2

            # move starting position to (i + 1, j + 1)
            start += 1
