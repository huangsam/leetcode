# https://leetcode.com/problems/contains-duplicate/

from collections import Counter


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Check if the input list contains any duplicates.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        return any(c > 1 for c in Counter(nums).values())
