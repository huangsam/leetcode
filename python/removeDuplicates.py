# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted array in-place.

        Complexity:
        - Time: O(n)
        - Space: O(1)

        Given an integer array nums sorted in non-decreasing order, remove
        the duplicates in-place such that each unique element appears only once.
        The relative order of the elements should be kept the same.

        Approach:
        - 0 or 1 is the base case
        - Numbers are already sorted in increasing order
        - Numbers are either duplicates or not
        - Iterate through numbers until a non-duplicate is found
        - Move non-duplicate over to next unique position
        - Return unique position + 1, since the offset starts at 0
        """
        if len(nums) <= 1:
            return len(nums)
        n_cur = 0
        n_uniq = 0
        while n_cur < len(nums):
            if nums[n_cur] != nums[n_uniq]:
                n_uniq += 1
                nums[n_uniq] = nums[n_cur]
            n_cur += 1
        return n_uniq + 1
