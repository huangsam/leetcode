# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = set()
        nlen = len(nums)
        sums = {}

        # Do initial caching
        for i in range(nlen):
            for j in range(nlen):
                if i != j:
                    sums[(i, j)] = nums[i] + nums[j]

        # Run an O(n^2) loop to find pairs that sum to -nums[k]
        for k in range(nlen):
            for key, val in sums.items():
                if nums[k] == -val:
                    i, j = key
                    if i != k and j != k:
                        res = tuple(sorted([nums[i], nums[j], nums[k]]))
                        solution.add(res)

        return sorted(list(res) for res in solution)
