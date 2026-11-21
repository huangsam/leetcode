# https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Find the longest common subsequence between two strings.

        The intuition for when things don't match:
        - [i-1][j]  -> drop text1[i-1], match against text2[:j]
        - [i][j-1]  -> drop text2[j-1], match against text1[:i]

        Complexity:
        - Time: O(n*m) where n = len(text1) and m = len(text2)
        - Space: O(n*m)
        """
        mat = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    mat[i][j] = 1 + mat[i - 1][j - 1]
                else:
                    mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

        return mat[len(text1)][len(text2)]
