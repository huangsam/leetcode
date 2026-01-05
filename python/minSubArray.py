# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    MAX_VALUE = 2**32

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)

        Slide left and right as you will. Right increases until
        the current_sum beats or matches the target. Left increases
        until the current_sum is lower than the target. Continue
        updating min_length in all cases. We return the minimum possible
        length at the end of the iteration.
        """
        left, right = 0, 0

        min_length = Solution.MAX_VALUE

        current_sum = 0

        while right < len(nums):
            current_sum += nums[right]
            right += 1
            while current_sum >= target:
                min_length = self._newMin(min_length, left, right)
                current_sum -= nums[left]
                left += 1

        if min_length == Solution.MAX_VALUE:
            return 0

        return min_length

    def _newMin(self, current: int, left: int, right: int) -> int:
        return min(current, right - left)
