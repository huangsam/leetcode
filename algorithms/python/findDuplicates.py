# https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        result = []
        for i in nums:
            if d.get(i, False):
                result.append(i)
            else:
                d[i] = True
        return result
