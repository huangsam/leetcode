# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Complexity:
        - Time: O(n)
        - Space: O(1)

        You are given an integer array nums. You are initially
        positioned at the array's first index, and each element
        in the array represents your maximum jump length at
        that position.

        Approach (efficient):
        - Assess jump power at every iteration
        - If we have negative jump power, then we cannot proceed
        - If a higher jump power exists, replace the previous one
        - Making it to the end implies we had enough jump power
        """
        jump_power = 0
        for idx, num in enumerate(nums):
            if jump_power < 0:
                return False
            if jump_power < num:
                jump_power = num
            if idx < len(nums) - 1:
                jump_power -= 1
        return True

    def canJumpDynamic(self, nums: List[int]) -> bool:
        """
        - Time: O(n^2)
        - Space: O(n)

        Approach (sub-efficient):
        - Initialize reachable array
        - Base case is reachable[0] = True
        - For each position i, mark i...i+n_val as reachable
        - Check if n_len-1 is reachable
        """
        if len(nums) <= 1:
            return True
        n_len = len(nums)
        reachable = [False] * n_len
        reachable[0] = True
        for n_idx, n_val in enumerate(nums):
            if reachable[n_idx] is False:
                continue
            for i in range(n_idx + 1, min(n_idx + n_val + 1, n_len)):
                reachable[i] = True
        return reachable[n_len - 1]
