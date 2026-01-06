# https://leetcode.com/problems/two-sum/

from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to a target value.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        # Keep track of the numbers we have seen so far and their indices
        seen_numbers: Dict[int, int] = {}

        # Return the index pairing that is expected for this function
        for idx, num in enumerate(nums):
            # Calculate the complement that we need to find
            complement = target - num

            # If the complement is already in the dictionary, we found our pair
            if complement in seen_numbers:
                return [seen_numbers[complement], idx]

            # Otherwise, store the current number with its index
            seen_numbers[num] = idx

        raise RuntimeError("There should be exactly one solution")
