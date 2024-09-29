from collections import defaultdict


# https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        s_letters: defaultdict[str, int] = defaultdict(int)
        for letter in s:
            s_letters[letter] += 1
        for letter in t:
            s_letters[letter] -= 1
        for key, val in s_letters.items():
            if val < 0:
                return key
        raise ValueError("There must be one difference between inputs")
