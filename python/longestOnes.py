from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Find the longest subarray by filling at most k zeros with ones.

        Use sliding window approach:
        - Expand the right pointer to include more elements.
        - If 0s in the current window exceeds k, move left pointer

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        max_ones = 0
        left = 0

        current_zeros = 0
        for right in range(left, len(nums)):
            if nums[right] == 0:
                current_zeros += 1

            # Move left pointer in such a way that we have enough zeros
            while current_zeros > k:
                if nums[left] == 0:
                    current_zeros -= 1
                left += 1

            # Get the largest valid interval
            max_ones = max(max_ones, right - left + 1)

        return max_ones
