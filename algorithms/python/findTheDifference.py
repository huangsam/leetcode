# https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_letters = {}
        for letter in s:
            if letter in s_letters:
                s_letters[letter] += 1
            else:
                s_letters[letter] = 1
        for letter in t:
            if letter in s_letters:
                s_letters[letter] -= 1
            else:
                s_letters[letter] = -1

        for key, val in s_letters.items():
            if val < 0:
                return key
