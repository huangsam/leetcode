# https://leetcode.com/problems/permutations/

from typing import List, Set


class Solution:
    def __init__(self) -> None:
        self.result: List[List[int]] = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Return all possible permutations of an array of distinct integers.

        Complexity:
        - Time: O(n! * n)
        - Space: O(n! * n)
        """
        self._helper(set(nums), [])
        return self.result

    def _helper(self, available: Set[int], arr: List[int]) -> None:
        if len(available) == 0:
            self.result.append(arr)
            return

        # We look at numbers in forward and backward directions
        for num in available:
            self._helper(available - {num}, arr + [num])
