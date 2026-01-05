# https://leetcode.com/problems/contains-duplicate-ii/

from typing import Dict, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Time: O(n)
        Space: O(n)
        
        1. Find all indices which have duplicates
        2. For each list of indices, see if any nC2 option satisfies
        3. Return True on first match. Return False with no matches

        Note that all indices are sorted so we're really looking at
        a subset of the nC2 options - where they are neighbors. Thus,
        we iterate idx[1] - idx[0], then idx[2] - idx[1] until we have
        exhausted all options.
        """
        val_latest_index: Dict[int, int] = {}

        for idx, num in enumerate(nums):
            if num not in val_latest_index:
                val_latest_index[num] = idx
                continue

            prev_idx = val_latest_index[num]
            if abs(idx - prev_idx) <= k:
                return True
            else:
                val_latest_index[num] = idx

        return False
