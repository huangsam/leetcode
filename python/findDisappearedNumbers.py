# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Find all numbers that disappeared from an array of size n.

        Use the array itself to mark presence: for each num, negate nums[abs(num)-1].

        Then iterate, if nums[i] > 0, i+1 is missing.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        n_len = len(nums)

        # Use the index of the array to mark the presence of numbers
        for i in range(n_len):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] *= -1

        # Collect the indices of the numbers that were not marked
        return [i + 1 for i in range(n_len) if nums[i] > 0]
