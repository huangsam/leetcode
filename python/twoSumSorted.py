# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        We know that there is exactly one solution and that the input
        list is sorted in increasing order. Then we know that the
        first item is min and last item is max. We start with min + max
        and see if that matches target. Then we adjust by trying
        different min/max values until the target hits.
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum < target:
                left += 1
            elif two_sum == target:
                # This tuple should have a 1-based index
                return [left + 1, right + 1]
            else:
                right -= 1
        raise RuntimeError("All test cases have one solution")
