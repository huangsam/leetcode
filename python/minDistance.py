# https://leetcode.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Find the minimum number of operations required to convert word1 to word2.

        The intuition for when things don't match:
        - [i-1][j-1] -> replace a char in word1
        - [i-1][j]   -> delete a char from word1
        - [i][j-1]   -> insert a char to word1

        Complexity:
        - Time: O(n * m) where n == len(word1) and m == len(word2)
        - Space: O(n * m)
        """
        mat = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            mat[i][0] = i

        for j in range(len(word2) + 1):
            mat[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    mat[i][j] = mat[i - 1][j - 1]
                else:
                    mat[i][j] = 1 + min(mat[i - 1][j - 1], mat[i - 1][j], mat[i][j - 1])

        return mat[len(word1)][len(word2)]
