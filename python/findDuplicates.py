# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List, Set


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Find all elements that appear twice in an array.

        Use a set to track numbers seen so far. For each number, if it's already in the set, add to result.

        This finds duplicates in O(n) time and space.

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
