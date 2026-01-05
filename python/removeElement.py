# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of a value from an array in-place.
        
        Complexity:
        - Time: O(n)
        - Space: O(1)

        Given an integer array nums and an integer val, remove all
        occurrences of val in nums in-place. The order of the elements
        may be changed. Then return the number of elements in
        nums which are not equal to val.

        Approach:
        - Ignore values after n_edit, they're not relevant
        - Assume that order of <= n_edit does not matter
        - When we find a mismatch, we add it to the left and raise n_edit
        - Return n_edit after all is said and done
        """
        n_cur = 0
        n_edit = 0
        while n_cur < len(nums):
            n_val = nums[n_cur]
            if n_val != val:
                nums[n_edit] = n_val
                n_edit += 1
            n_cur += 1
        return n_edit
