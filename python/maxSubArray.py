# https://leetcode.com/problems/maximum-subarray/

from typing import Any, List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the contiguous subarray with the largest sum.

        To perform better than O(n^2), we recognize that if the current sum
        drops below 0, it cannot contribute to a larger sum in the future.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        max_sum: Any = float("-inf")
        current_sum = 0

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            # If current_sum drops below 0, reset it
            if current_sum < 0:
                current_sum = 0

        return max_sum
