# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays in logarithmic time.

        The idea is to use a helper function `get_kth` that finds the k-th smallest
        element in the combined sorted array formed by nums1 and nums2. We can use
        this function to find the median directly.

        Complexity:
        - Time: O(log(m + n))
        - Space: O(log(m + n))
        """
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2

        # Helper to find the k-th smallest element (1-indexed)
        def get_kth(k, start1, start2):
            # Base Cases
            if start1 >= n1:
                return nums2[start2 + k - 1]
            if start2 >= n2:
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])

            # Look at the middle of the 'k' we are searching for
            mid = k // 2
            # Use float('inf') if we run out of elements in one array
            val1 = nums1[start1 + mid - 1] if start1 + mid <= n1 else float("inf")
            val2 = nums2[start2 + mid - 1] if start2 + mid <= n2 else float("inf")

            if val1 < val2:
                # nums1's first 'mid' elements cannot be the k-th smallest
                return get_kth(k - mid, start1 + mid, start2)
            else:
                # nums2's first 'mid' elements cannot be the k-th smallest
                return get_kth(k - mid, start1, start2 + mid)

        # For even totals, median is average of two middle elements
        if total % 2 == 1:
            return float(get_kth(total // 2 + 1, 0, 0))
        else:
            left = get_kth(total // 2, 0, 0)
            right = get_kth(total // 2 + 1, 0, 0)
            return (left + right) / 2.0
