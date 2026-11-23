# https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        Check if the given list of integers can be partitioned into two
        subsets such that the sum of elements in both subsets is equal.

        The key intuition is that we are measuring for cumulative
        reachability and midpoint should be the target sum.

        Complexity:
        - Time: O(n * t) where t is the target sum
        - Space: O(t) where t is the target sum
        """
        n_sum = sum(nums)
        if len(nums) == 1 or n_sum % 2 == 1:
            return False

        mid = n_sum // 2
        mem = [False] * (mid + 1)
        mem[0] = True

        for num in nums:
            # Each mem[s] is a target that is reachable or not
            for s in range(mid, num - 1, -1):
                mem[s] = mem[s] or mem[s - num]
                if mem[s] is True and s == mid:
                    return True

        return False
