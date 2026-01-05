# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List, Set


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        seen: Set[int] = set()
        result = []
        for num in nums:
            # An integer appears twice
            if num in seen:
                result.append(num)
            # An integer appears at least once
            else:
                seen.add(num)
        return result
