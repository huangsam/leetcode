# https://leetcode.com/problems/valid-anagram/
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        An Anagram is a word or phrase formed by rearranging
        the letters of a different word or phrase, using all
        the original letters exactly once.
        """
        s_count = defaultdict(int)
        for ch in s:
            s_count[ch] += 1
        for ch in t:
            s_count[ch] -= 1
        return all(v == 0 for v in s_count.values())
