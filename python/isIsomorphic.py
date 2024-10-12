# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Assume that the length of s and t are identical and non-empty.

        We will traverse the characters of s and t, one by one. Each
        char in s will be mapped to a char in t until a) there is a
        mapping mismatch or b) the entirety of s and t have been
        iterated. We return false for a, true for b.
        """
        # To check for discrepancies in mapping
        mapping = {}

        # To see what was mapped before
        mapped = set()

        for ch_s, ch_t in zip(s, t):
            if ch_s not in mapping:
                # No two characters may map to the same char
                if ch_t in mapped:
                    return False

                mapping[ch_s] = ch_t
                mapped.add(ch_t)

            # One char cannot be mapped to 2+ chars
            elif mapping[ch_s] != ch_t:
                return False

        return True
