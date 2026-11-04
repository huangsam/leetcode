# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Check if the string `s` matches the pattern `p`.

        This implementation uses dynamic programming with memoization to efficiently
        check all possible matches between the string and the pattern.

        Complexity:
        - Time: O(m * n)
        - Space: O(m * n)
        """
        memo: dict[tuple[int, int], bool] = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            # If pattern is exhausted, string must also be exhausted
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")

            # Case: Next character is '*'
            if j + 1 < len(p) and p[j + 1] == "*":
                # Branch 1: Skip '*' and its preceding character (0 matches)
                # Branch 2: Consume one char of s if first_match is True
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Case: Standard single character or '.' match
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
