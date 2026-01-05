# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array with duplicates.
        
        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                # Minimum is in the right half (excluding mid)
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                # Minimum is in the left half (including mid)
                hi = mid
            else:
                # Cannot determine, reduce search space
                hi = hi - 1
        return nums[lo]
