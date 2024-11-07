# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.00

        if n < 0:
            x = 1 / x
            n = abs(n)

        result = 1.00

        while n > 0:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result
