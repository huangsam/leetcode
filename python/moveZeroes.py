# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Tracks position of the next non-zero element
        non_zero_found = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_found] = nums[non_zero_found], nums[i]

                # Increment for the next non-zero element
                non_zero_found += 1
