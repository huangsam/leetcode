# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Complexity:
        - Time: O(log(n))
        - Space: O(1)
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]:
                return mid

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
        return -1
