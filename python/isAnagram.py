# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determine if two strings are anagrams.

        An Anagram is a word or phrase formed by rearranging the letters of a
        different word or phrase, using all the original letters exactly once.

        Use Counter to count frequencies of characters in both strings and compare.

        Complexity:
        - Time: O(n + m)
        - Space: O(n)
        """
        return Counter(s) == Counter(t)
