# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Return the max amount of money you can rob without alerting the police.
        Recall that adjacent houses have security systems connected and will
        alert if two adjacent houses were broken into on the same night.

        Through reasoning, it can be said that to avoid the police:
        - n-2 + current is what you'd hit for each night
        - n-1 + skip is an alternative
        """
        if len(nums) == 1:
            return nums[0]

        day_1 = nums[0]
        day_2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(nums[i] + day_1, day_2)
            day_1 = day_2
            day_2 = temp

        return day_2
