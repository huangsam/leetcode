# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Find the index where a target would be inserted in a sorted array.


        Similar to regular binary search. But the main difference
        in this case is that we are looking for an insert position
        between two numbers (for middle case) or an insert position
        on either side. For the left side, checking for midpoint set
        to zero is sufficient. For the right side, returning the lo
        pointer is sufficient since it should be only one number
        higher than the highest number possible.

        Complexity:
        - Time: O(log(n))
        - Space: O(1)
        """
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                # Note that the list values are distinct
                if mid == 0 or nums[mid - 1] < target:
                    return mid
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
