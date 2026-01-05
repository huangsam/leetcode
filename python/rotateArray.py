# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Complexity:
        - Time: O(n)
        - Space: O(1)

        Given an integer array nums, rotate the array to the
        right by k steps, where k is non-negative.

        Try to come up with as many solutions as you can.
        Could you do it in-place with O(1) extra space?

        Approach:
        - Reverse all numbers to correct positions in reverse order
        - Reverse k numbers back to correct order
        - Reverse remainder back to correct order
        """
        if k < 0:
            raise ValueError("Assume k is non-negative")
        op_count = k % len(nums)
        n = len(nums) - 1
        self._reverse(nums, 0, n)
        self._reverse(nums, 0, op_count - 1)
        self._reverse(nums, op_count, n)

    def _reverse(self, nums: List[int], a: int, b: int) -> None:
        while a < b:
            nums[a], nums[b] = nums[b], nums[a]
            a, b = a + 1, b - 1
