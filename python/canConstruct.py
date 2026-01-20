# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determine if a ransom note can be constructed from magazine letters.

        Use Counter to count frequencies of characters in both strings and check
        if ransom note frequencies are covered by magazine frequencies.

        Complexity:
        - Time: O(n + m)
        - Space: O(n)
        """
        ransom_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)
        return all(ransom_freq[ch] <= magazine_freq[ch] for ch in ransom_freq)
