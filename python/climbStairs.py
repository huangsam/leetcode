# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb n stairs.

        This problem is equivalent to finding the nth Fibonacci number, as
        the number of ways to reach step n is the sum of ways to reach step
        n-1 and n-2. Use an iterative approach with two variables to compute
        it efficiently in O(n) time and O(1) space.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        if n <= 1:
            return 1

        # The solution is very similar to the bottoms-up DP approach
        # for fibonacci. To save on space, we use two variables
        # instead of a Python list
        f1, f2 = 1, 1
        for _ in range(2, n + 1):
            current = f1 + f2
            f1 = f2
            f2 = current

        return f2
