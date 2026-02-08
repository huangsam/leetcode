# https://leetcode.com/problems/contains-duplicate/

from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the input list contains any duplicates.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        return any(c > 1 for c in Counter(nums).values())
