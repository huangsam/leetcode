# https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    def __init__(self) -> None:
        self.result: List[List[int]] = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Time: O(C(n, k) * k)
        Space: O(C(n, k) * k)
        """
        self._helper(n, k, [])
        return self.result

    def _helper(self, n: int, k: int, nums: List[int]) -> None:
        if k == 0:
            self.result.append(nums)
            return

        # Only look forward to avoid duplicates
        start = nums[-1] + 1 if nums else 1

        # Traverse start to n with enough buffer for k items
        for i in range(start, n - k + 2):
            self._helper(n, k - 1, nums + [i])
