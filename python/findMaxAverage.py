# https://leetcode.com/problems/maximum-average-subarray-i/

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Given an array consisting of n integers, find the contiguous subarray of
        length k that has the maximum average value and return this value.

        We use a sliding window technique to keep track of the current sum of the
        last k elements as we iterate through the array. We update the maximum sum
        whenever we find a new maximum.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(k, len(nums)):
            # Remove the old value
            cur_sum -= nums[i - k]

            # Add the new value
            cur_sum += nums[i]

            # Keep track of the latest maximum
            max_sum = max(max_sum, cur_sum)

        # k is always constant, so max sum -> max avg
        return max_sum / k
