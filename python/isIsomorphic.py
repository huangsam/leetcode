# https://leetcode.com/problems/isomorphic-strings/

from typing import Dict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determine if two strings are isomorphic.

        Complexity:
        - Time: O(n)
        - Space: O(n)

        Assume that the length of s and t are identical and non-empty.

        We will traverse the characters of s and t, one by one. Each
        char in s will be mapped to a char in t until a) there is a
        mapping mismatch or b) the entirety of s and t have been
        iterated. We return false for a, true for b.
        """
        # To check for discrepancies in mapping
        s_to_t: Dict[str, str] = {}
        t_to_s: Dict[str, str] = {}

        for ch_s, ch_t in zip(s, t):
            # Check if s->t mapping exists and matches
            if ch_s in s_to_t:
                if s_to_t[ch_s] != ch_t:
                    return False
            else:
                s_to_t[ch_s] = ch_t

            # Check if t->s mapping exists and matches (bijection)
            if ch_t in t_to_s:
                if t_to_s[ch_t] != ch_s:
                    return False
            else:
                t_to_s[ch_t] = ch_s

        return True
