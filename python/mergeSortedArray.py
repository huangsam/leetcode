# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        You are given two integer arrays nums1 and nums2, sorted in
        non-decreasing order, and two integers m and n, representing
        the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]

        Approach:
        - Start from back at nums1[m+n-1]
        - Add max of nums1[i] and nums2[j] until either one runs out
        - Add leftover of nums2 if any items remain
        - There is nothing to do for leftover of nums1, so we're done
        """
        if n == 0:
            return
        n1_cur = m - 1
        n2_cur = n - 1
        n1_edit = m + n - 1
        while n1_cur >= 0 and n2_cur >= 0:
            if nums1[n1_cur] > nums2[n2_cur]:
                nums1[n1_edit] = nums1[n1_cur]
                n1_cur -= 1
            else:
                nums1[n1_edit] = nums2[n2_cur]
                n2_cur -= 1
            n1_edit -= 1
        while n2_cur >= 0:
            nums1[n1_edit] = nums2[n2_cur]
            n2_cur -= 1
            n1_edit -= 1
