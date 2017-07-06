# https://leetcode.com/problems/hamming-distance/
class Solution(object):
    def getBinary(self, val):
        return bin(val)[2:][::-1]

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        x = self.getBinary(x)
        y = self.getBinary(y)
        x_len, y_len = len(x), len(y)
        x_ind, y_ind = 0, 0
        while x_ind < x_len and y_ind < y_len:
            if x[x_ind] != y[y_ind]:
                distance += 1
            x_ind += 1
            y_ind += 1
        while x_ind < x_len:
            if x[x_ind] == '1':
                distance += 1
            x_ind += 1
        while y_ind < y_len:
            if y[y_ind] == '1':
                distance += 1
            y_ind += 1
        return distance
