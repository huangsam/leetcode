# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort an array with values 0, 1, and 2 in-place.

        Use Dutch flag algorithm with three pointers: lo (next 0 position), mid
        (current), hi (next 2 position).

        If nums[mid] == 0, swap with lo and increment lo and mid.
        If 2, swap with hi and decrement hi.
        If 1, increment mid.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            # If the current element is 0, swap it with the element at lo
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            # If the current element is 1, just move to the next element
            elif nums[mid] == 1:
                mid += 1
            # If the current element is 2, swap it with the element at hi
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
