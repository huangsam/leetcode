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
        # Store the initial mapping that we'll use to check nums with
        complement_map = {target - val: idx for idx, val in enumerate(nums)}

        # Return the index pairing that is expected for this function
        for idx, val in enumerate(nums):
            if new_idx := complement_map.get(val):
                # If the same element is used twice, don't bother
                if new_idx != idx:
                    # The index pairing is of size 2
                    return [new_idx, idx]

        raise RuntimeError("There should be exactly one solution")
