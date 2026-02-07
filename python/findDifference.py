# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Given two 0-indexed integer arrays nums1 and nums2, return a list
        answer of size 2 where [0] has distinct integers in nums1 which
        are not present in nums2 and [1] has distinct integers in nums2 which
        are not present in nums1.

        Complexity:
        - Time: O(n + m)
        - Space: O(n + m)
        """
        x = set(nums1)
        y = set(nums2)
        return [list(x - y), list(y - x)]
