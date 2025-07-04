# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


# TODO: Make this solution more efficient
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = self._merge(nums1, nums2)
        alen = len(arr)
        middle = ((1 + len(arr)) // 2) - 1
        if alen % 2 == 0:
            left, right = middle, middle + 1
            answer = float(arr[left] + arr[right]) / 2.0
        else:
            answer = arr[middle]
        return answer

    def _merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nlen1 = len(nums1)
        nlen2 = len(nums2)
        c1, c2 = 0, 0
        arr = []
        while c1 < nlen1 and c2 < nlen2:
            if nums1[c1] <= nums2[c2]:
                arr.append(nums1[c1])
                c1 += 1
            else:
                arr.append(nums2[c2])
                c2 += 1
        arr += nums1[c1:]
        arr += nums2[c2:]
        return arr
