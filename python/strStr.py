# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time: O(n * m)
        Space: O(1)
        """        """
        Start from the beginning. Whenever there is a match of needle in
        haystack, then we start iterating and keep track of index. If there
        is a full match, then we store the minimum result, as we are looking
        for the first occurrence of needle. If we end up with no match,
        we will return -1 instead of a non-negative integer.
        """
        # End result that we're looking for
        match_at = -1

        # The size of the full match required to get needle
        needle_size = len(needle)

        # The progress that we're making towards a needle
        needle_prog = 0

        # Initial starting point
        ptr = 0

        # Iterate through the whole haystack for a needle
        while ptr < len(haystack):
            # Increment progress if a match occurs
            if haystack[ptr] == needle[needle_prog]:
                needle_prog += 1

            # Or reset progress and pointer if a match does not occur
            else:
                ptr = ptr - needle_prog + 1
                needle_prog = 0
                continue

            # Update pointer, otherwise loop will run forever!
            ptr += 1

            # If we found a full match, update result and reset progress
            if needle_prog == needle_size:
                # Note that we must handle the initial case and nth case
                match_at = ptr - needle_prog if match_at == -1 else min(match_at, ptr - needle_prog)
                needle_prog = 0

        return match_at
