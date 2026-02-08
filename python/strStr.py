# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find the first occurrence of a substring in a string.

        To make this more optimized, we can either implement Rabin-Karp or
        simply leverage haystack.find(needle) for linear performance.

        Complexity:
        - Time: O(n * m)
        - Space: O(m)
        """
        m, n = len(needle), len(haystack)

        # Escape if needle is bigger
        if m > n:
            return -1

        # Find needle in haystack
        for left in range(n - m + 1):
            if haystack[left] != needle[0]:
                continue
            if haystack[left : left + m] == needle:
                return left

        # Fallback answer when no match is found
        return -1
