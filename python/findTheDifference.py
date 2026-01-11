# https://leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Find the letter that was added to string t.

        Use an array to count the frequency of each lowercase letter in s and t.
        Since t has one extra character, increment counts for s and decrement
        for t, then find the character with count -1.

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
