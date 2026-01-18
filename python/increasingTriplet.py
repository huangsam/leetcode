# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Check if there exists a triplet (i, j, k) such that
        nums[i] < nums[j] < nums[k] with i < j < k.

        The O(n^3) brute-force approach would involve three nested loops
        to check all triplet combinations.

        The O(n^2) approach would involve two nested loops to find pairs
        and then check for a third element.

        However, we can achieve this in O(n) time and O(1) space
        by maintaining two variables to track the smallest and second smallest
        elements found so far.

        Complexity:
        - Time: O(n), where n is the length of nums.
        - Space: O(1)
        """
        first = second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
