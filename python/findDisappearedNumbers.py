# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Find all numbers that disappeared from an array of size n.

        Use the array itself to mark presence: for each num, negate nums[abs(num)-1].

        Then iterate, if nums[i] > 0, i+1 is missing.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        result = []

        # Use the index of the array to mark the presence of numbers
        n_len = len(nums)
        for i in range(n_len):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] *= -1

        # Collect the indices of the numbers that were not marked
        n_len = len(nums)
        for i in range(n_len):
            if nums[i] > 0:
                result.append(i + 1)

        return result
