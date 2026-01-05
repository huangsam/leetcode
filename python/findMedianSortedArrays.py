# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Complexity:
        - Time: O(log(min(m, n)))
        - Space: O(1)
        """
        # Ensure nums1 is the shorter array for efficient binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m  # Binary search on nums1's partition

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            # Determine elements around partitionX
            # If partitionX is 0, nothing on left, so maxLeftX is -infinity
            # If partitionX is m, nothing on right, so minRightX is +infinity
            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float("inf") if partitionX == m else nums1[partitionX]

            # Determine elements around partitionY
            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float("inf") if partitionY == n else nums2[partitionY]

            # Check if partitions are correct
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Found the correct partition
                if (m + n) % 2 == 0:
                    # Even number of elements
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    # Odd number of elements
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                # partitionX is too far right, need to move left
                high = partitionX - 1
            else:  # maxLeftY > minRightX
                # partitionX is too far left, need to move right
                low = partitionX + 1

        # This part should ideally not be reached if inputs are valid
        return 0.0  # Or raise an error
