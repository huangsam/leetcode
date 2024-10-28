# https://leetcode.com/problems/permutations/

from typing import List, Set


class Solution:
    def __init__(self) -> None:
        self.result: List[List[int]] = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.helper(set(nums), [])
        return self.result

    def helper(self, available: Set[int], arr: List[int]) -> None:
        if len(available) == 0:
            self.result.append(arr)
            return
        for num in available:
            self.helper(available - {num}, arr + [num])
