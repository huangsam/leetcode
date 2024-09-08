# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Look for characters of s in t in an orderly fashion. Ignore
        characters that do not match. Keep a counter of characters in
        s that match. If we have the counter match the length of s, then
        we return true. Otherwise, we return false.
        """
        # How many characters in s that match
        char_count = 0

        # Iterate through all of t
        for ch in t:
            # If we find a char match, then continue through. Note
            # that we only do this if s actually has letters
            if s and s[char_count] == ch:
                char_count += 1

            # If we match the subsequence, then skip searching
            if char_count == len(s):
                return True

        # Handles special case of s and t being empty
        return char_count == len(s)
