# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Handle target - nums[i] with a new dictionary where you have
        the remainder as the key and the index as the value.

        Then with the new dictionary, check the values of nums to see
        if there is a match. If the match is related to a value of num
        whose index is not matching with the key-value pair, then we have
        the answer we want.

        Assume there is exactly one solution for any of the provided inputs.
        """
        mapping = {}

        # Store the initial mapping that we'll use to check nums with
        for idx, num in enumerate(nums):
            mapping[target - num] = idx

        # Return the index pairing that is expected for this function
        for idx, num in enumerate(nums):
            # If the two numbers don't add up, don't bother
            if num not in mapping:
                continue

            other_idx = mapping[num]

            # If the same element is used twice, don't bother
            if other_idx == idx:
                continue

            # The index pairing is of size 2
            return [idx, other_idx]

        raise RuntimeError("There should be exactly one solution")
