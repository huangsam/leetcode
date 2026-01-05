# https://leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        # For lowercase English letters
        counts = [0] * 26

        for letter in s:
            counts[ord(letter) - ord("a")] += 1
        for letter in t:
            idx = ord(letter) - ord("a")
            counts[idx] -= 1
            if counts[idx] < 0:
                return letter

        raise ValueError("There must be one difference between inputs")
