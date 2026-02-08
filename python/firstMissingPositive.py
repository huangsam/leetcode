# https://leetcode.com/problems/first-missing-positive/

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Find the smallest missing positive integer in an unsorted array.

        We can achieve O(n) time and O(1) space by using the input array itself
        to track which numbers are present. The idea is to place each number
        in its "correct" position (i.e., 1 at index 0, 2 at index 1, etc.).
        After rearranging, the first index that doesn't have the correct
        number indicates the missing positive integer.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        n = len(nums)

        # Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its target position
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

        # After rearrangement, find the first index where the number is not correct
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are correct, the missing integer is n + 1
        return n + 1
