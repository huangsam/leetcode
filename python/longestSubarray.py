# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Find the longest subarray of 1s after deleting one element.

        Use sliding window approach:
        - Expand the right pointer to include more elements.
        - If more than one zero in the current window, move left pointer
        - We must delete one element, so the length is right - left

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        left = 0
        longest = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1 and left < right:
                # Only change the count upon zero
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Erase an item in the range via exclusion
            longest = max(longest, right - left)

        return longest
