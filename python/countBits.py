# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Count the number of 1 bits for every number from 0 to n.

        Get the binary representation for each number i from
        0..n using dynamic programming with the bottoms-up
        approach.

        If i is even, i can be written as 2k, where k is
        shifted right by one bit and the LSB is 0.

        If i is odd, i can be written as 2k + 1, where k is
        shifted right by one bit and the LSB is 1.

        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + (i % 2)
        return dp
