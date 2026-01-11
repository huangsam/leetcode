# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find two lines that together with x-axis form a container with most water.

        Use two pointers, i at start, j at end. Compute area = (j - i) * min(height[i], height[j]), update max.

        Move the pointer with the smaller height inward to potentially find larger area.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        i, j = 0, len(height) - 1  # Start from both ends
        water = 0
        while i < j:
            # Area = width * min height
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1  # Move the shorter line
            else:
                j -= 1
        return water
