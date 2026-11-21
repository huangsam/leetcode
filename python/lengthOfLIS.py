# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Return the length of the longest increasing subsequence in the
        given list of integers.

        This is a case where the mem[i] is computed conditionally so
        our return value is the maximum of all mem[i] values.

        Complexity:
        - Time: O(n^2)
        - Space: O(n)
        """
        mem = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                # This is the case where j < i and nums[j] < nums[i]
                # which results in an increasing subsequence
                if nums[j] < nums[i]:
                    mem[i] = max(mem[i], 1 + mem[j])
        return max(mem) if mem else 0
