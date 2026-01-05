# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Complexity:
        - Time: O(log(n))
        - Space: O(1)
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                # Minimum is in the right half (excluding mid)
                lo = mid + 1
            else:
                # Minimum is in the left half (including mid)
                hi = mid
        return nums[lo]
