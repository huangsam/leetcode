# https://leetcode.com/problems/contains-duplicate-ii/

from typing import Dict, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Determine if there are two distinct indices i and j in the array such that
        nums[i] == nums[j] and abs(i - j) <= k.

        This problem requires checking for duplicates within a sliding window of size k.
        A naive approach would be to check all pairs, but that's O(n^2).

        Optimal approach: Use a hash map to track the most recent index of each number.
        As we iterate through the array:
        - If a number is not in the map, add it with its current index.
        - If it is in the map, check if the difference between current index and stored index <= k.
            - If yes, return True.
            - If no, update the map with the current index (to keep the most recent occurrence).

        This works because we only need to track the latest index for each number. If a duplicate
        is found but the distance > k, we update to the current index, effectively sliding the window.

        Complexity:
        - Time: O(n) - single pass through the array
        - Space: O(min(n, unique_elements)) - worst case O(n) if all elements are unique
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
