# https://leetcode.com/problems/next-permutation/


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Find the next lexicographical permutation of the given list of numbers in-place.

        Do not return anything, modify nums in-place instead.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        n = len(nums)

        # 1. Find the pivot: first element from the right where nums[i] < nums[i + 1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. If a pivot exists, find the smallest element > nums[i] on its right and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse the descending suffix nums[i + 1 : n] in-place
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
