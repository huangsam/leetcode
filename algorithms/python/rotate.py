# https://leetcode.com/problems/rotate-image/description/
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m_len = len(matrix)
        # squares
        for x in range(m_len // 2):
            # elements
            for y in range(x, m_len - x - 1):
                north = matrix[x][y]
                # top <- left
                matrix[x][y] = matrix[m_len - y - 1][x]
                # left <- bottom
                matrix[m_len - y - 1][x] = matrix[m_len - x - 1][m_len - y - 1]
                # bottom <- right
                matrix[m_len - x - 1][m_len - y - 1] = matrix[y][m_len - x - 1]
                # right <- top
                matrix[y][m_len - x - 1] = north
