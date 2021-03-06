# https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = set()
        nlen = len(nums)
        sums = {}
        for i in range(nlen):
            for j in range(nlen):
                if i != j:
                    sums[(i, j)] = nums[i] + nums[j]
        for k in range(nlen):
            for key, val in sums.iteritems():
                if nums[k] == -val:
                    i, j = key
                    if i != k and j != k:
                        res = tuple(sorted([nums[i], nums[j], nums[k]]))
                        solution.add(res)
        return sorted([res for res in solution])
