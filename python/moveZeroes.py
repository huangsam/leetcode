# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        # Tracks position of the next non-zero element
        non_zero_found = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_found] = nums[non_zero_found], nums[i]

                # Increment for the next non-zero element
                non_zero_found += 1

    def moveZeroesSingleWrite(self, nums: List[int]) -> None:
        """
        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        slow = 0

        # First partition: fill in non-zero elements
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # Optimization: Only write if the pointers are actually different
                if slow != fast:
                    nums[slow] = nums[fast]
                slow += 1

        # Second partition: fill in zeros where needed
        while slow < len(nums):
            # Optimization: Only write if the value isn't already zero
            if nums[slow] != 0:
                nums[slow] = 0
            slow += 1
