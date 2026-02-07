# https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Return true if word1 and word2 are close, and false otherwise.

        Two strings are close if you can attain one from the other via:

        Operation 1: Swap any two existing characters.

        Operation 2: Transform every occurrence of one existing character
        into another existing character, and do the same with the other character.

        Complexity:
        - Time: O(n + m)
        - Space: O(n + m)
        """
        w1_freq = Counter(word1)
        w2_freq = Counter(word2)

        # Tip: keys() acts like sets under the hood
        if w1_freq.keys() != w2_freq.keys():
            return False

        # Tip: distribution of frequencies != set of frequencies
        if Counter(w1_freq.values()) != Counter(w2_freq.values()):
            return False

        return True
