# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            # Handle duplicate elements at the boundaries
            while lo < hi and nums[lo] == nums[lo + 1]:
                lo += 1
            while hi > lo and nums[hi] == nums[hi - 1]:
                hi -= 1

            mid = (lo + hi) // 2
            if target == nums[mid]:
                return True

            # Case 1: The left half is sorted
            if nums[lo] <= nums[mid]:
                # Target is inside this sorted left half
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                # Target is outside this sorted left half
                else:
                    lo = mid + 1

            # Case 2: The right half is sorted
            else:
                # Target is inside this sorted right half
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                # Target is outside this sorted right half
                else:
                    hi = mid - 1
        return False
