# https://leetcode.com/problems/find-pivot-index/

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Find the pivot index of an array, where sum to the left of the index
        is equal to sum to the right of the index. Return -1 otherwise.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        total_sum = sum(nums)
        left_sum = 0

        for i, j in enumerate(nums):
            # The right sum excludes the current element and left sum
            if left_sum == total_sum - j - left_sum:
                return i
            left_sum += j

        # Default answer if we cannot find anything
        return -1
