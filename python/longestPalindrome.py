# https://leetcode.com/problems/longest-palindromic-substring/

from typing import Tuple


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        longest_start = 0
        longest_length = 0

        for i in range(len(s)):
            # Odd length palindromes (e.g., "aba")
            # The returned indices will be (start, end_inclusive)
            start1, end1 = self._longestAroundCenter(s, i, i)
            len1 = end1 - start1 + 1

            # Even length palindromes (e.g., "abba")
            start2, end2 = self._longestAroundCenter(s, i, i + 1)
            len2 = end2 - start2 + 1

            # Determine which palindrome (odd or even) is longer for the current center
            if len1 > len2:
                current_start = start1
                current_length = len1
            else:
                current_start = start2
                current_length = len2

            # Update the overall longest palindrome if the current one is longer
            if current_length > longest_length:
                longest_length = current_length
                longest_start = current_start

        return s[longest_start : longest_start + longest_length]

    def _longestAroundCenter(self, s: str, left: int, right: int) -> Tuple[int, int]:
        # Expand outwards from the center(s)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # At this point, `left` is one position to the left of the actual palindrome start,
        # and `right` is one position to the right of the actual palindrome end.
        # So, the actual start index is `left + 1`
        # and the actual end index (inclusive) is `right - 1`.
        return (left + 1, right - 1)
