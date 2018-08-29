# https://leetcode.com/problems/power-of-four/description/
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 4 == 0:
            num = num / 4
        return num == 1
