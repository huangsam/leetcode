# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
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

    def canJumpOriginal(self, nums: List[int]) -> bool:
        """
        Approach (sub-efficient):
        - Initialize reachable array
        - Base case is reachable[0] = True
        - For each position i, mark i..i+nval as reachable
        - Check if nlen-1 is reachable
        """
        if len(nums) <= 1:
            return True
        nlen = len(nums)
        reachable = [False] * nlen
        reachable[0] = True
        for nidx, nval in enumerate(nums):
            if reachable[nidx] is False:
                continue
            for i in range(nidx + 1, min(nidx + nval + 1, nlen)):
                reachable[i] = True
        return reachable[nlen - 1]
