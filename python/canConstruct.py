# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determine if a ransom note can be constructed from magazine letters.

        We are going to collect the mapping of character frequencies
        for ransom note. Then we subtract the frequencies when iterating
        through magazine. If ransom mapping has all values <= 0, then we
        are good to construct the ransom note.

        Complexity:
        - Time: O(n + m)
        - Space: O(n)
        """
        ransom_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)
        return all(ransom_freq[ch] <= magazine_freq[ch] for ch in ransom_freq)
